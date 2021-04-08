import argparse
import io
import os
import re
import sys

import docker
import pandas as pd
from tqdm.auto import tqdm


def find_all_dockerfiles(path, recursive=False):
    ipynb_regex = re.compile(r"^Dockerfile\..*$")
    if not recursive:
        dockerfiles = [os.path.join(path, x) for x in os.listdir(path) if ipynb_regex.fullmatch(x)]
        dockerfiles = [x for x in dockerfiles if os.path.isfile(x)]
        return dockerfiles
    dockerfiles = []
    for address, dirs, files in os.walk(path, topdown=True):
        dockerfiles.extend([os.path.join(address, x) for x in files if ipynb_regex.fullmatch(x)])
    return dockerfiles


def find_table(readme):
    with open(readme, "r") as f:
        raw_lines = f.readlines()
    lines = list(map(str.strip, raw_lines))
    table_start = lines.index(".. csv-table::") + 3
    table_end = lines.index("", table_start)
    header = lines[table_start - 2][len(":header: "):]
    table = [header] + lines[table_start:table_end]
    table = pd.read_csv(io.StringIO("\n".join(table)))

    return {'table': table, 'table_start': table_start}


def merge_tables(current_table, new_table):
    table = current_table.merge(new_table, left_on=current_table.columns[0], right_on='Dockerfile', how='left',
                                suffixes=('_old', ''))
    table.drop(columns=[x for x in table.columns if x.endswith('_old')], inplace=True)
    table.sort_values('Size', inplace=True)
    table['Size'] = table['Size'].apply(lambda x: f"{x:.4g}") + " MB"
    return table


def write_table(readme, table, table_start):
    s = io.StringIO()
    table.to_csv(s, index=False, header=False)

    with open(readme, 'r') as f:
        raw_lines = f.readlines()

    lines = raw_lines[:table_start]
    for prev_line, new_line in zip(raw_lines[table_start:], s.getvalue().split("\n")):
        new_line = prev_line.replace(prev_line.strip(), new_line.strip())
        lines.append(new_line)
    lines.extend(raw_lines[table_start + len(table) + 1:])
    with open(readme, 'w') as f:
        f.writelines(lines)


def update_table(readme, table):
    result = find_table(readme)
    table = merge_tables(result['table'], table)
    write_table(readme, table, result['table_start'])


def get_filenames(dockerfiles):
    return [os.path.basename(x) for x in dockerfiles]


def get_docker_size(path, client):
    image, _ = client.images.build(path=os.path.dirname(path), dockerfile=os.path.basename(path), tag="tiny-python")
    size = image.attrs['Size'] / (1024 * 1024)
    version = client.containers.run(image, "--version", remove=True, stdout=True, stderr=False)
    version = version.decode('utf-8').strip().split()[1]
    return size, version


def main(args):
    dockerfiles = find_all_dockerfiles(args.folder, recursive=args.recursive)
    client = docker.from_env()
    sizes = []
    versions = []
    with tqdm(dockerfiles, unit='file') as progress_bar:
        for dockerfile in progress_bar:
            progress_bar.set_postfix({'dockerfile': os.path.basename(dockerfile)})
            size, version = get_docker_size(dockerfile, client)
            sizes.append(size)
            versions.append(version)
    table = pd.DataFrame({'Dockerfile': get_filenames(dockerfiles), 'Size': sizes, 'Python Version': versions})
    update_table(args.readme, table)
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update readme file according to docker sizes')
    parser.add_argument('readme', type=str, help='path to README.rst')
    parser.add_argument('folder', type=str, default=".", help='folder with Dockerfiles')
    parser.add_argument('-r', '--recursive', action='store_true', help='find Dockerfiles in folders recursively')
    args = parser.parse_args()
    sys.exit(main(args))
