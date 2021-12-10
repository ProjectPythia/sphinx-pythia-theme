# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path
from urllib import request

sys.path.append(os.path.abspath("../"))

# -- Project information -----------------------------------------------------

project = "Sphinx Pythia Theme"
copyright = "2021"
author = "The Project Pythia Contributors"
release = "2021.12.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "ablog",
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinxext.opengraph",
    "sphinx_click.ext",
    "sphinx_inline_tabs",
    "sphinx_panels",
    "sphinx_pythia_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.parsers.rst.directives.body.Sidebar"),
]

suppress_warnings = ["myst.domains", "ref.ref"]

numfig = True

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "substitution",
]

panels_add_bootstrap_css = False

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_pythia_theme"
html_theme_path = ["../"]
html_logo = "images/dummy_logo_dark.svg"
html_title = "Sphinx Pythia Theme"
html_copy_source = True
html_sourcelink_suffix = ""
html_favicon = "images/favicon.ico"
html_last_updated_fmt = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

jupyter_execute_notebooks = "cache"
thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "repository_branch": "master",
}

html_theme_options = {
    "theme_dev_mode": True,
    "path_to_docs": "docs",
    "repository_url": "https://github.com/executablebooks/sphinx-book-theme",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com/",
        "notebook_interface": "classic",
        "thebe": True,
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "logo_only": True,
    "show_toc_level": 2,
    "domnav": [
        {
            "content": "Theme",
            "url": "/this-theme",
        },
        {
            "content": "GitHub",
            "url": "https://github.com/ProjectPythia/sphinx-pythia-theme",
        },
    ],
    "page_layouts": {
        "index": "banner",
    },
    "footer": {
        "logos": {
            "NCAR": "images/NCAR-contemp-logo-blue.svg",
            "Unidata": "images/Unidata_logo_horizontal_1200x300.svg",
            "UAlbany": "images/UAlbany-A2-logo-purple-gold.svg",
        },
        "acknowledgement": {
            "content": (
                "This material is based upon work supported by the National Science Foundation "
                "under Grant Nos. 2026863 and 2026899. Any opinions, findings, and conclusions "
                "or recommendations expressed in this material are those of the author(s) and "
                "do not necessarily reflect the views of the National Science Foundation."
            ),
            "image": "images/nsf-logo.png",
        },
    },
}

# -- Download kitchen sink reference docs -------------------------------------
# These are the kitchen sink files used by the Sphinx Themes gallery at
# https://github.com/sphinx-themes/sphinx-themes.org
# To re-download, delete the `references/kitchen-sink` folder and build the docs
kitchen_sink_files = [
    "api.rst",
    "index.rst",
    "lists-and-tables.rst",
    "paragraph-markup.rst",
]
for ifile in kitchen_sink_files:
    path_file = Path(f"kitchen-sink/{ifile}")
    path_file.parent.mkdir(exist_ok=True)
    if not path_file.exists():
        print(f"Downloading kitchen sink file {ifile}")
        resp = request.urlopen(
            f"https://github.com/sphinx-themes/sphinx-themes.org/raw/master/sample-docs/kitchen-sink/{ifile}"  # noqa
        )
        header = ".. DOWNLOADED FROM sphinx-themes.org, DO NOT MANUALLY EDIT\n"
        path_file.write_text(header + resp.read().decode())
