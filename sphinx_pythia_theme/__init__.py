import os

__version__ = "0.0.1"

def setup(app):
    if hasattr(app, 'add_html_theme'):
        theme_path = os.path.abspath(os.path.dirname(__file__))
        app.add_html_theme('pythia', os.path.join(theme_path, 'pythia'))
