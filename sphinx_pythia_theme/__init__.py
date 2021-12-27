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


def add_functions_to_context(app, pagename, templatename, context, doctree):

    def _is_div_section(tag):
        return tag.name == 'div' and tag.has_attr('class') and 'section' in tag['class']

    def _new_tag_like(tag):
        if isinstance(tag, BeautifulSoup):
            return BeautifulSoup()
        elif isinstance(tag, NavigableString):
            return copy.copy(tag)
        else:
            tag_copy = tag.find_parents()[-1].new_tag(tag.name)
            tag_copy.attrs = copy.copy(tag.attrs)
            return tag_copy

    def _children_of(tag):
        return [] if isinstance(tag, NavigableString) else tag.children

    def _denest_sections_from(tag, maxdepth=2, _depth=1, order=True):
        new_tag = _new_tag_like(tag)
        new_tags = [new_tag]
        for child in _children_of(tag):
            if _is_div_section(child) and _is_div_section(tag) and _depth < maxdepth:
                new_tags.extend(_denest_sections_from(child, maxdepth=maxdepth, _depth=_depth+1, order=order))
                if order:
                    new_tag = _new_tag_like(tag)
                    del new_tag['id']
                    new_tags.append(new_tag)
            else:
                new_tag.extend(_denest_sections_from(child, maxdepth=maxdepth, _depth=_depth, order=order))
        return new_tags

    def denest_sections(html, maxdepth=2, preserve_order=True):
        soup = BeautifulSoup(html, 'html.parser')
        new_soup = _new_tag_like(soup)
        for child in soup.children:
            new_soup.extend(_denest_sections_from(child, maxdepth=maxdepth, order=preserve_order))
        return str(new_soup)

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

    if "footer_logos" in config:
        logos_config = config["footer_logos"]

        for key in logos_config:
            image = logos_config[key]
            logos_config[key] = copy_image(app, image)


def fix_theme_options(app, pagename, templatename, context, doctree):
    context["theme_denest_depth"] = int(context.get("theme_denest_depth", 2))

    order = context.get("theme_denest_order", "True").lower()
    context["theme_denest_order"] = False if order == "false" else True


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
