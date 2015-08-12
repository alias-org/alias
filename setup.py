#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='ALIAS',
    description='ALIAS',
    author='Roberto La Greca',
    license='GNU',
    url='https://github.com/alias-org/alias.git',
    author_email='roberto@robertolagreca.com',
    version='0.1',
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=[''],
    packages=find_packages(exclude=['docs', 'tests*']),
    extras_require={
        'inout': ['pyparsing', 'networkx'],
        'db' : ['sqlalchemy', 'py2neo']
    },
    tests_require=['nose'],
)
