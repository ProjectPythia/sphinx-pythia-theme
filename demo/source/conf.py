#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import shutil
import sys

# -- Project information -----------------------------------------------------

project = 'Project Pythia'
author = 'Project Pythia Developers & Contributors'
copyright = f'2020-{datetime.datetime.now().year}, {author}'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Define what extensions will parse which kind of source file
source_suffix = {
    '.rst': 'restructuredtext',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_pythia_theme'
html_last_updated_fmt = '%d %B %Y'

# Logo & Title
html_logo = '_static/logo.svg'
html_title = ''

# Favicon
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# HTML Theme-specific Options
html_theme_options = {
    'onepagers': {
        'index': {
            'background': '_static/background.jpg',
            'attribution': 'Photo by Jeff Stapleton from Pexels',
        },
    },
    'navbar': {
        'Card 1': 'index.html#card-1',
        'Card 2': 'index.html#card-2',
        'Card 3': 'index.html#card-3',
        'Card 4': 'index.html#card-4',
        'Github': 'https://github.com',
    },
    'logobar': {
        'steampunk-wings': '_static/steampunk-wings-logo.jpg',
        'horse': '_static/horse-logo2.jpg',
        'globe-compass': '_static/globe-compass-logo.jpg',
    },
    'sponsor': {
        'text': 'This material is based upon work supported by the National Science Foundation under Grant No. XXXXXXX. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.',
        'logo': '_static/sponsor.png',
    },
}
