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

    Dockerfile.scratch-minimal,Minimal Python image with almost no libraries from scratch,4.762 MB,3.10.5
    Dockerfile.scratch-full,Smallest Python image with default libraries from scratch,32.84 MB,3.10.5
    Dockerfile.haizaar-minimal,Stripped official Python image (`haizaar/python-minimal`_),33.67 MB,3.10.6
    Dockerfile.python-alpine,Python Alpine-based Official,48.7 MB,3.10.6
    Dockerfile.alpine,Alpine-based,53.38 MB,3.10.5
    Dockerfile.ubuntu,Ubuntu-based,107.3 MB,3.10.4
    Dockerfile.python-slim,Minimal packages needed to run python,126 MB,3.10.6
    Dockerfile.python,Python Debian-based Official with a lot of packages,922 MB,3.10.6

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
