#!/usr/bin/env python3
import os, sys
import cfgsaver
from cfgsaver import __version__, __description__, __author__, __email__, __license__, __title__
from setuptools import setup, find_packages
from setuptools.command.install import install
#from subprocess import check_call
#from pkg_resources import Requirement, resource_filename
from distutils.dir_util import copy_tree
#import shutil

app_name = "cfgsaver"
pkg_name = "cfgsaver"

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

s = setup(
	name=app_name,
	version=__version__,
	license=__license__,
	description=__description__,
	long_description=read("README.md"),
	long_description_content_type='text/markdown',
	url='https://github.com/prahladyeri/%s' % app_name,
	packages=find_packages(),
	include_package_data=True,
	install_requires=[],
	python_requires = ">= 3.4",
	author=__author__,
	author_email=__email__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	)

