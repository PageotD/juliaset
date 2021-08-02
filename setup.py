# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='juliaset',
    version='0.2.0',
    description='Sample package for JuliaSet',
    long_description=readme,
    author='Damien Pageot',
    author_email='damien.pageot@gmail.com',
    url='https://github.com/PageotD/juliaset',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires=">=3.8"
)