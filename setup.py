#!/usr/bin/env python
# -*- coding: utf-8 -*-
from glob import glob
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, 'alias')
import release
version = release.write_versionfile()
sys.path.pop(0)

packages = ["alias",
            "alias.classes"
            "alias.inout"
            "alias.semantics"]

package_data = []

config = {
    'description': 'ALIAS',
    'author': 'Roberto La Greca',
    'url': 'https://github.com/roberto-lagreca/alias',
    'download_url': 'https://github.com/roberto-lagreca/alias/archive/master.zip',
    'author_email': 'roberto@robertolagreca.com',
    'version': '0.1',
    'install_requires': [],
    'test_suite' : 'nose.collector',
    'tests_require' : ['nose>=0.10.1'],
    'packages': packages,
    'scripts': [],
    'name': 'ALIAS'
}

setup(**config)
