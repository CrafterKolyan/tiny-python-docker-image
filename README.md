# Tiny Python Docker image
The most lightweight python docker image possible

## Possible variants
| Dockerfile   | Description | Size |
| :----------- | :--- | :--: |
| Dockerfile.scratch-minimal | Minimal Python image with almost no libraries from scratch | 6.08 MB |
| Dockerfile.scratch-full | Smallest Python image with default libraries from scratch | 41.5 MB |
| Dockerfile.python-alpine | Python Alpine-based Official | 44.7 MB |
| Dockerfile.alpine | Alpine-based | 49.2 MB |
| Dockerfile.ubuntu | Ubuntu-based | 106 MB |
| Dockerfile.python-slim | Minimal packages needed to run python | 114 MB |
| Dockerfile.python | Python Debian-based Official with a lot of packages | 885 MB |

## Building image
```bash
docker build -t python-tiny . -f <Dockerfile name>
```
For example:
```bash
docker build -t python-tiny . -f Dockerfile.python-alpine
```


## Running image
```bash
docker run --rm -it python-tiny
```
