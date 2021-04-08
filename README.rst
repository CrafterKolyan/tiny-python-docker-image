Tiny Python Docker image
========================

The most lightweight Python 3 Docker image possible

Possible variants
-----------------

.. list-table::
   :header-rows: 1

   * - Dockerfile
     - Description
     - Size

   * - Dockerfile.scratch-minimal
     - Minimal Python image with almost no libraries from scratch
     - 6.08 MB
   * - Dockerfile.scratch-full
     - Smallest Python image with default libraries from scratch
     - 41.5 MB
   * - Dockerfile.python-alpine
     - Python Alpine-based Official
     - 44.7 MB
   * - Dockerfile.alpine
     - Alpine-based
     - 49.2 MB
   * - Dockerfile.ubuntu
     - Ubuntu-based
     - 106 MB
   * - Dockerfile.python-slim
     - Minimal packages needed to run python
     - 114 MB
   * - Dockerfile.python
     - Python Debian-based Official with a lot of packages
     - 885 MB

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

  docker run --rm -it python -tiny

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