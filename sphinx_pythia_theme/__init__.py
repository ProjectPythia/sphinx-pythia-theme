import copy
import os
import re
import shutil
from pathlib import Path
from pkg_resources import get_distribution, DistributionNotFound

from bs4 import BeautifulSoup, NavigableString
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


def copy_config_images(app):
    if hasattr(app.config, "html_theme_options"):
        config = app.config.html_theme_options
    else:
        return

    if "footer_logos" in config:
        logos_config = config["footer_logos"]

        for key in logos_config:
            image = logos_config[key]
            logos_config[key] = copy_image(app, image)


def fix_theme_options(app, pagename, templatename, context, doctree):
    context["theme_denest_depth"] = int(context.get("theme_denest_depth", 2))

    order = context.get("theme_denest_split", "True").lower()
    context["theme_denest_split"] = False if order == "false" else True


def add_functions_to_context(app, pagename, templatename, context, doctree):

    def denest_sections(html, maxdepth=2, split=True):
        if maxdepth < 2:
            return html

        soup = BeautifulSoup(html, 'html.parser')

        hnames = [f'h{i}' for i in range(2, maxdepth+1)]
        htags = soup.find_all(hnames)
        htags.sort(key=lambda x: x.name)

        for htag in htags:

            div_section = htag.find_parent('div', {'class': 'section'})
            if div_section is None:
                continue

            div_parent = div_section.parent

            if split:
                div_remainder = soup.new_tag(div_parent.name)
                div_remainder.attrs = copy.copy(div_parent.attrs)
                del div_remainder['id']
                remainder = [sibling for sibling in div_section.next_siblings]
                div_remainder.extend(remainder)

            div_section = div_section.extract()

            div_parent.insert_after(div_section)

            if split:
                div_section.insert_after(div_remainder)

        return str(soup)

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


def setup(app: Sphinx):
    app.require_sphinx("3.5")
    app.add_html_theme("sphinx_pythia_theme", get_html_theme_path())
    app.add_directive("banner", Banner)
    app.connect("builder-inited", copy_config_images)
    app.connect("html-page-context", fix_theme_options)
    app.connect("html-page-context", add_functions_to_context)

    return {
        "version": "0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
