sphinxcontrib-email
===================

|badge:pypi-version| |badge:py-versions|
|badge:pre-commit| |badge:pre-commit.ci|
|badge:black| |badge:prettier|

.. |badge:pypi-version| image:: https://img.shields.io/pypi/v/sphinxcontrib-email.svg
   :target: https://pypi.org/project/sphinxcontrib-email
   :alt: [Latest PyPI version]
.. |badge:py-versions| image:: https://img.shields.io/pypi/pyversions/sphinxcontrib-email.svg
   :target: https://pypi.org/project/sphinxcontrib-email
   :alt: [Supported Python versions]
.. |badge:pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: [pre-commit: enabled]
.. |badge:pre-commit.ci| image:: https://results.pre-commit.ci/badge/github/sphinx-contrib/email/master.svg
   :target: https://results.pre-commit.ci/latest/github/sphinx-contrib/email/master
   :alt: [pre-commit.ci status]
.. |badge:black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: [Code style: black]
.. |badge:prettier| image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg
   :target: https://github.com/prettier/prettier
   :alt: [Code style: prettier]

This package provides ``sphinxcontrib.email``, an email obfuscator for
Sphinx-based documentation.

Installation
------------

1. ``pip install sphinxcontrib-email``

Configuration
-------------

1. Add ``'sphinxcontrib.email'`` to the ``extensions`` list in ``conf.py``.

   .. code::

      extensions = [ 'sphinxcontrib.email' ]


Usage
-----

Auto Mode
^^^^^^^^^

In ``conf.py``, set

.. code::

   email_automode = True

to automatically obfuscate all ``mailto`` links.


Manual Mode
^^^^^^^^^^^

To obfuscate an email address use the ``email`` role:

.. code::

   :email:`Name Surname <user@myplace.org>`

Renders as "Name Surname" with the appropriate mailto link.

.. code::

   :email:`user@myplace.org`

Renders as "user@myplace.org" with the appropriate mailto link
