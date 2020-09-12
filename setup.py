# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

f = open('README.rst', 'r')
try:
    long_desc = f.read()
finally:
    f.close()

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-email',
    version='0.1',
    url='https://github.com/sphinx-contrib/email',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-email',
    license = 'BSD-3',
    license_files = 'LICENSE',
    author='Christian Knittl-Frank',
    author_email='lcnittl@gmail.com',
    description='Sphinx email obfuscation extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
