#!/usr/bin/env python

#
# Used by distutils.
# https://docs.python.org/2/distutils/introduction.html
# https://docs.python.org/2/distutils/setupscript.html
#

from distutils.core import setup

setup(
    name='DarkZero',
    version='1.0',
    description='Dark Zero',
    author='Alien Labs',
    author_email='info@alienlabs.io',
    url='https://github.com/richburdon/dark-zero',
    setup_requires=['nose>=1.0'],
    packages=[]
)
