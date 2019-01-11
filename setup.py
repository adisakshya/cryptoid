"""
Module Name: setup.py
Author: Adisakshya Chauhan
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'cryptographer',
    'author': 'Adisakshya Chauhan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'adisakshya chauhan',
    'version': '1.0',
    'install_requires': ['nose','Crypto'],
    'packages': ['crypto'],
    'scripts': ['bin/crypto.py'],
    'name': 'crypto'
    }

setup(**config)
