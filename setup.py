#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='python-utils',
    version='0.0.2',
    description='Modilabs Shared Python Utilities',
    author='Modilabs',
    author_email='info@modilabs.org',
    url='http://modilabs.org/',
    packages = find_packages(exclude=['*.pyc']),
    install_requires = [
        "python-dateutil"
    ],
)
