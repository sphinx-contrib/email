sphinxcontrib-email
===================

|badge:pre-commit| |badge:black| |badge:prettier|

This package provides sphinxcontrib.email, an email obfuscator for
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

To obfuscate an email address use something like:

.. code::

   :email:`Name Surname <user@myplace.org>`

Renders as "Name Surname" with the appropriate mailto link.

.. code::

   :email:`user@myplace.org`

Renders as "user@myplace.org" with the appropriate mailto link


.. |badge:pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: [pre-commit: enabled]
.. |badge:black| image:: https://img.shields.io/badge/code%20style-black-000000
   :target: https://github.com/psf/black
   :alt: [Code style: black]
.. |badge:prettier| image:: https://img.shields.io/badge/code_style-prettier-ff69b4
   :target: https://github.com/prettier/prettier
   :alt: [Code style: prettier]
