# Tiny Python Docker image
The most lightweight python docker image possible

## Possible variants
| Dockerfile   | Idea | Size |
| :----------- | :--- | :--: |
| Dockerfile.ubuntu2004 | Ubuntu 20.04 based python 3 | 139 MB |

## Building image
```bash
docker build -t tiny-python-docker-image . -f <Dockerfile name>
```
For example:
```bash
docker build -t tiny-python-docker-image . -f Dockerfile.ubuntu2004
```


## Running image
```bash
docker container run --rm -it tiny-python-docker-image
```