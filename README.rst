Tiny Python Docker image
========================

The most lightweight Python 3 Docker image possible.

.. image:: https://github.com/CrafterKolyan/tiny-python-docker-image/actions/workflows/update-repository.yml/badge.svg?branch=main
    :target: https://github.com/CrafterKolyan/tiny-python-docker-image/actions/workflows/update-repository.yml

Possible variants
-----------------

.. csv-table::
    :header: Dockerfile,Description,Size,Version
    :widths: 10, 70, 10, 10

    Dockerfile.scratch-minimal,Minimal Python image with almost no libraries from scratch,7.27 MB,3.12.7
    Dockerfile.scratch-full,Smallest Python image with default libraries from scratch,22.92 MB,3.12.7
    Dockerfile.haizaar-minimal,Stripped official Python image (`haizaar/python-minimal`_),35.25 MB,3.13.0
    Dockerfile.alpine,Alpine-based,48.19 MB,3.12.7
    Dockerfile.python-alpine,Python Alpine-based Official,50.27 MB,3.13.0
    Dockerfile.ubuntu,Ubuntu-based,116.7 MB,3.12.3
    Dockerfile.python-slim,Minimal packages needed to run python,120 MB,3.13.0
    Dockerfile.python,Python Debian-based Official with a lot of packages,1017 MB,3.13.0

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
