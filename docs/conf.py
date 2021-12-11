# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import subprocess
import sys

# -- Project information -----------------------------------------------------

author = "The Project Pythia Community"
copyright = "2021"
language = None

# -- General configuration ---------------------------------------------------

exclude_patterns = ["**.ipynb_checkpoints", ".DS_Store", "Thumbs.db", "_build"]

execution_allow_errors = False
execution_excludepatterns = []
execution_in_temp = False
execution_timeout = 30

external_toc_exclude_missing = False
external_toc_path = "../book/_toc.yml"

pygments_style = "sphinx"

suppress_warnings = ["myst.domains"]

templates_path = ["_templates"]

# -- Extensions configuration ------------------------------------------------

extensions = [
    "ablog",
    "myst_nb",
    "sphinx_click.ext",
    "sphinx_comments",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_external_toc",
    "sphinx_inline_tabs",
    "sphinx_panels",
    "sphinx_thebe",
    "sphinx_togglebutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxext.opengraph",
]

comments_config = {"hypothesis": False, "utterances": False}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

jupyter_cache = ""
jupyter_execute_notebooks = "cache"

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]
myst_substitutions = {"sub3": "My _global_ value!"}
myst_url_schemes = ["mailto", "http", "https"]

nb_output_stderr = "show"

nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.parsers.rst.directives.body.Sidebar"),
]

numfig = True

panels_add_bootstrap_css = False

thebe_config = {
    "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
    "repository_branch": "master",
}

use_jupyterbook_latex = True
use_multitoc_numbering = True

# -- Options for HTML output -------------------------------------------------

html_copy_source = True
html_favicon = "images/favicon.ico"
html_last_updated_fmt = ""
html_logo = "images/dummy_logo_dark.svg"
html_sourcelink_suffix = ""
html_static_path = ["_static"]
html_theme = "sphinx_pythia_theme"
html_title = "Sphinx Pythia Theme"

html_theme_options = {
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
        {"content": "Documentation", "url": "/this-theme"},
        {
            "content": "GitHub",
            "url": "https://github.com/ProjectPythia/sphinx-pythia-theme",
        },
    ],
    "page_layouts": {"index": "banner"},
    "footer": {
        "logos": {
            "NCAR": "images/NCAR-contemp-logo-blue.svg",
            "Unidata": "images/Unidata_logo_horizontal_1200x300.svg",
            "UAlbany": "images/UAlbany-A2-logo-purple-gold.svg",
        },
        "acknowledgement": {
            "content": (
                "This material is based upon work supported by the National "
                "Science Foundation under Grant Nos. 2026863 and 2026899. Any "
                "opinions, findings, and conclusions or recommendations expressed "
                "in this material are those of the author(s) and do not necessarily "
                "reflect the views of the National Science Foundation."
            ),
            "image": "images/nsf-logo.png",
        },
    },
}

# ==============================================================================

subprocess.run([sys.executable, "../book/getkitchensink.py", "."])
