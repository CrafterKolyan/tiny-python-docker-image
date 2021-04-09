Tiny Python Docker image
========================

The most lightweight Python 3 Docker image possible.

.. image:: https://github.com/CrafterKolyan/tiny-python-docker-image/actions/workflows/update-readme-table.yml/badge.svg?branch=main
    :target: https://github.com/CrafterKolyan/tiny-python-docker-image/actions/workflows/update-readme-table.yml

Possible variants
-----------------

.. csv-table::
    :header: Dockerfile,Description,Size,Version

    Dockerfile.scratch-minimal,Minimal Python image with almost no libraries from scratch,6.082 MB,3.8.8
    Dockerfile.scratch-full,Smallest Python image with default libraries from scratch,41.48 MB,3.8.8
    Dockerfile.python-alpine,Python Alpine-based Official,44.7 MB,3.9.4
    Dockerfile.alpine,Alpine-based,49.18 MB,3.8.8
    Dockerfile.ubuntu,Ubuntu-based,105.6 MB,3.8.5
    Dockerfile.python-slim,Minimal packages needed to run python,114.5 MB,3.9.4
    Dockerfile.python,Python Debian-based Official with a lot of packages,885.5 MB,3.9.4

Requirements
------------
- Docker

Usage
-----
Building image
``````````````
.. code-block:: bash

    docker build -t python-tiny . -f <Dockerfile name>

For example:

.. code-block:: bash

    docker build -t python-tiny . -f Dockerfile.python-alpine

Running image
`````````````
.. code-block:: bash

  docker run --rm -it python-tiny

Technologies
------------
- Docker
- :code:`ldd` (prints the shared libraries required by each program or shared library specified on the command line): used to create :code:`scratch-full` and :code:`scratch-minimal` images.

Related links
-------------
- https://xebia.com/blog/how-to-create-the-smallest-possible-docker-container-of-any-image/
- https://xebia.com/blog/create-the-smallest-possible-docker-container/

Related projects
----------------
- https://github.com/jfloff/alpine-python
- https://github.com/haizaar/docker-python-minimal
