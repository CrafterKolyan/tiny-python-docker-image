Tiny Python Docker image
========================

The most lightweight Python 3 Docker image possible.

.. image:: https://github.com/CrafterKolyan/tiny-python-docker-image/actions/workflows/update-readme-table.yml/badge.svg?branch=main
    :target: https://github.com/CrafterKolyan/tiny-python-docker-image/actions/workflows/update-readme-table.yml

Possible variants
-----------------

.. csv-table::
    :header: Dockerfile,Description,Size,Version
    :widths: 10, 70, 10, 10

    Dockerfile.scratch-minimal,Minimal Python image with almost no libraries from scratch,5.347 MB,3.10.11
    Dockerfile.scratch-full,Smallest Python image with default libraries from scratch,33.65 MB,3.10.11
    Dockerfile.haizaar-minimal,Stripped official Python image (`haizaar/python-minimal`_),37.56 MB,3.11.3
    Dockerfile.alpine,Alpine-based,56.23 MB,3.10.11
    Dockerfile.python-alpine,Python Alpine-based Official,56.74 MB,3.11.3
    Dockerfile.ubuntu,Ubuntu-based,107.3 MB,3.10.6
    Dockerfile.python-slim,Minimal packages needed to run python,127.6 MB,3.11.3
    Dockerfile.python,Python Debian-based Official with a lot of packages,919.5 MB,3.11.3

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

    docker build -t python-tiny . -f Dockerfile.scratch-full

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

.. _haizaar/python-minimal: https://github.com/haizaar/docker-python-minimal
