#!/usr/bin/env python
from setuptools import setup
from codecs import open
from os import path


def readme():
    with open("README.md", "r") as infile:
        return infile.read()


classifiers = [
    # Pick your license as you wish (should match "license" above)
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]
setup(
    name="ms_drf_utils",
    version="0.0.1",
    description="Global Micro-services DRF utilities package",
    author="Damien Lopa",
    author_email="damien@lopa.io",
    packages=["ms_drf_utils"],
    url="https://github.com/damienLopa/ms_drf_utils",
    license="MIT",
    keywords="django restframework drf utils base",
    long_description=readme(),
    classifiers=classifiers,
    long_description_content_type="text/markdown",
)
