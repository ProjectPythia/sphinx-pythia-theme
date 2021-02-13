import os
from pathlib import Path

from sphinx.application import Sphinx

__version__ = "0.0.1"


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(Path(__file__).parent)
    return theme_path


def setup(app: Sphinx):
    app.add_html_theme('sphinx_pythia_theme', get_html_theme_path())
