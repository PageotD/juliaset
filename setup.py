# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os.path
import codecs

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.readline()

setup(
    name='juliaset',
    version=get_version("juliaset/__init__.py"),
    description='Sample package for JuliaSet',
    long_description=readme,
    author='Damien Pageot',
    author_email='damien.pageot@gmail.com',
    url='https://github.com/PageotD/juliaset',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires=">=3.8"
)