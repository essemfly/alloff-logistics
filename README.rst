================
Logistics Server
================

.. contents::

Installation
============

Requirements
------------

- `poetry`_
- python 3.9^
- env files (ask teammate!)

.. _poetry:
   https://python-poetry.org/

Install dependencies
--------------------

.. code-block:: bash

    git clone https://github.com/lessbutter/logistics-server.git
    cd logistics-server
    poetry install


If you are first run, database migration is required
----------------------------------------------------

.. code-block:: bash

    poetry run ./managy.py migrate

Run server
==========

.. code-block:: bash

    poetry activate
    poetry shell

    # then
    python manage.py runserver # default port 8000

OR

.. code-block:: bash

    poetry run ./manage.py runserver


Run gRPC server
---------------

.. code-block:: bash

    poetry run ./manage.py grpcrunserver --dev # default port 50051
