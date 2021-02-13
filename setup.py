import os
from setuptools import setup, find_packages

from sphinx_pythia_theme import __version__

with open('README.md', 'rt') as fobj:
    long_description = fobj.read()

setup(
    name="sphinx-pythia-theme",
    version=__version__,
    description="Sphinx Pythia Theme.",
    long_description=long_description,
    url="https://github.com/ProjectPythia/sphinx-pythia-theme",
    author="Kevin Paul",
    author_email="kpaul@ucar.edu",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ],

    install_requires=[
        "setuptools",
    ],
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_pythia_theme = sphinx_pythia_theme',
        ]
    },
    packages=find_packages(),
    include_package_data=True,
)