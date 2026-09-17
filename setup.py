#!/usr/bin/env python3

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "olll",
    version = "0.1.0",
    author = "OLLL collaboration",
    author_email="",
    python_requires='>=3.10',
    install_requires=["onnx>=1.10.0", "onnxruntime>=1.20.0", "numpy>=2.0.0", "pyyaml"],
    description="Neural network adapter for LHC likelihood interpretation",
    license="GPLv3",
    url="https://github.com/OpenML-LHClikelihoods/",
    py_modules=["nnAdapter", "nnPreprocessing", "metadataValidator" ],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
