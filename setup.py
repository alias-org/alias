try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ALIAS',
    'author': 'Roberto La Greca',
    'url': 'https://github.com/roberto-lagreca/alias',
    'download_url': 'https://github.com/roberto-lagreca/alias/archive/master.zip',
    'author_email': 'roberto@robertolagreca.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ALIAS'
}

setup(**config)
