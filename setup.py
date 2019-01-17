"""
Module Name: setup
Author: Adisakshya Chauhan
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'cryptographer',
    'author': 'Adisakshya Chauhan',
    'url': 'https://github.com/adisakshya/cryptoid',
    'download_url': 'https://github.com/adisakshya/cryptoid',
    'author_email': 'adisakshya98@gmail.com',
    'version': '1.0',
    'install_requires': ['nose','Crypto'],
    'packages': ['cryptoid'],
    'scripts': ['bin/cryptoid.py'],
    'name': 'cryptoid'
    }

setup(**config)
