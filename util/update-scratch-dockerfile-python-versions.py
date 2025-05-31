import argparse
import re
import sys

import requests
from packaging import version

python_version_regex = re.compile(r"^(ARG\s+PYTHON_VERSION=).*$")


def find_latest_python_alpine_version():
    select_regex = re.compile(r"<select[^>]* name=\"branch\"[^>]*>([\s\S]*?)</select>")
    session = requests.session()
    response = session.get("https://pkgs.alpinelinux.org/packages?name=python3")
    text = response.text
    matches = select_regex.findall(text)
    match len(matches):
        case 0:
            raise ValueError(f"Didn't find branch on the website response")
        case 1:
            regex_match = matches[0]
        case _:
            raise ValueError(f"Found two or more branches on the website response: {matches!r}")
    option_regex = re.compile(r"<option[^>]*>([\s\S]*?)</option>")
    matches = option_regex.findall(regex_match)
    match len(matches):
        case 0:
            raise ValueError(f"Didn't find options on the website response")
    matches = [x.strip() for x in matches]
    options = [x for x in matches if x.startswith("v")]
    versions = sorted(options, key=lambda x: version.parse(x[1:]), reverse=True)

    for version_ in versions:
        print(f"Looking at alpine version: {version_}")
        url = f"https://pkgs.alpinelinux.org/packages?name=python3&branch={version_}&repo=main&arch=&maintainer="
        print(url)
        response = session.get(url)
        text = response.text
    
        version_regex = re.compile(r"<td[^>]* class=\"version\"[^>]*>([\s\S]*?)</td>")
        matches = version_regex.findall(text)
        match len(matches):
            case 0:
                continue
            case _:
                break
    else:
        raise ValueError(f"Didn't find versions on the website response")
    matches = [x.strip() for x in matches]

    tag_regex = re.compile(r"<[^>]*>([\s\S]*?)</[^>]*>")
    new_matches = []
    for x in matches:
        match = tag_regex.fullmatch(x)
        if match is None:
            raise ValueError("Couldn't match on version code to find version text: {x!r}")
        new_matches.append(match.group(1))
    matches = new_matches
    del new_matches

    versions = [version.parse(x) for x in matches]
    release_versions = set(x.release[:2] for x in versions)
    printable_versions = [str.join(".", map(str, x)) for x in release_versions]
    match len(printable_versions):
        case 0:
            raise ValueError(f"BUG: Impossible case. Couldn't find any release version")
        case 1:
            printable_version = printable_versions[0]
        case _:
            raise ValueError(f"Multiple python versions. Can't select one: {printable_versions}")
    return printable_version

def update_python_version(filepath, version):
    with open(filepath, 'r', encoding='utf8') as f:
        raw_lines = f.readlines()
    updated_lines = raw_lines
    for i, line in enumerate(raw_lines):
        regex_match = python_version_regex.match(line)
        if regex_match:
            new_line = regex_match.group(1) + version + "\n"
            updated_lines = raw_lines[:i] + [new_line] + raw_lines[i+1:]
            break
    with open(filepath, 'w', encoding='utf8') as f:
        f.writelines(updated_lines)



def main(filepaths):
    latest_python_version = find_latest_python_alpine_version()
    print(f"Latest python version in alpine repository: {latest_python_version}")
    for filepath in filepaths:
        update_python_version(filepath, latest_python_version)
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update Dockerfile scratch files ')
    parser.add_argument('file', type=str, nargs='+', help='path to scratch files')
    args = parser.parse_args()
    sys.exit(main(args.file))
