# -*- coding: utf-8 -*-

import os
import re
import sys
from setuptools import setup

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(PROJECT_ROOT, 'sqlalchemy_eventsource', '__init__.py')
    with open(filename) as f:
        contents = f.read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)

setup(
    name='SQLAlchemy-EventSource',
    version=get_version(),
    description='',
    long_description=__doc__,
    url='https://github.com/vaiski/sqlalchemy-eventsource',
    author='',
    license='MIT',
    zip_safe=False,
    packages=['sqlalchemy_eventsource'],
    install_requires=[
        'six',
        'SQLAlchemy>=1.0'
    ],
    extras_require={
        'test': [
            'pytest',
            'pylint',
            'flake8'
        ]
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Database'
    ]
)
