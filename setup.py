#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 18 13:34:23 2025

@author: did
"""

from setuptools import setup, find_packages

setup(
    name="jsonviewer",
    version="0.1.0",
    author="Didier Flamm",
    author_email="did_padman@hotmail.com",
    description="Un visualiseur JSON TUI et console avec Rich et Textual",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url= "https://github.com/DidierFlamm",
    packages=find_packages(),
    install_requires=[
        "rich>=13.0.0",
        "textual>=0.27.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "jsonviewer = run_viewer:main",
        ],
    },
)
