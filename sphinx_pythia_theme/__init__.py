import os
import re
import shutil
from pathlib import Path
from pkg_resources import get_distribution, DistributionNotFound

from bs4 import BeautifulSoup as bs
from sphinx.application import Sphinx

from .banner import Banner

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = "0.0.0"


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(Path(__file__).parent)
    return theme_path


def add_functions_to_context(app, pagename, templatename, context, doctree):

    def denest_sections(html):
        soup = bs(html, "html.parser")

        def parent_section(tag):
            if tag.name != 'div': # must be a div
                return False
            elif not tag.has_attr('class') or 'section' not in tag['class']: # must match div.section
                return False
            elif not tag.find('div', {'class': 'section'}): # must contain a div.section
                return False
            else:
                return True

        for s in soup.find_all(parent_section):
            ss = [s]
            for s_ in s.find_all('div', {'class': 'section'}, recursive=False):
                ss.extend(['\n', s_.extract()])
            s.replace_with(*ss)

        return re.sub(r'\n+', '\n', str(soup))

    context["denest_sections"] = denest_sections


def copy_image(app, image):
    conf_dir = Path(app.confdir)
    out_dir = Path(app.outdir)
    old_img = conf_dir / image
    if old_img.is_file():
        new_dir = out_dir / "_images"
        os.makedirs(new_dir, exist_ok=True)
        new_img = Path(new_dir) / old_img.name
        shutil.copy(old_img, new_img)
        return str(Path("_images") / old_img.name)
    else:
        raise FileNotFoundError(f"Image file not found: {old_img}")


def copy_config_images(app):
    if hasattr(app.config, "html_theme_options"):
        config = app.config.html_theme_options
    else:
        return

    if "footer" in config:
        footer_config = config["footer"]

        if "logos" in footer_config:
            for key in footer_config["logos"]:
                image = footer_config["logos"][key]
                footer_config["logos"][key] = copy_image(app, image)

        if "acknowledgement" in footer_config:
            if "image" in footer_config["acknowledgement"]:
                image = footer_config["acknowledgement"]["image"]
                footer_config["acknowledgement"]["image"] = copy_image(app, image)


def setup(app: Sphinx):
    app.require_sphinx("3.5")
    app.add_html_theme("sphinx_pythia_theme", get_html_theme_path())
    app.add_directive("banner", Banner)
    app.connect("builder-inited", copy_config_images)
    app.connect("html-page-context", add_functions_to_context)

    return {
        "version": "0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
