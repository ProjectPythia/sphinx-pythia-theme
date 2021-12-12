import os
import shutil
from pathlib import Path

from bs4 import BeautifulSoup as bs
from sphinx.application import Sphinx

from .banner import Banner

__version__ = "2021.12.1"


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(Path(__file__).parent)
    return theme_path


def add_functions_to_context(app, pagename, templatename, context, doctree):
    def _denest_sections(html):
        soup = bs(html, "html.parser")
        sections = []
        for h1 in soup.find_all(["h1"]):
            sections.append(h1.parent)
            for child in h1.parent.children:
                if (child.name == "section") or (
                    child.name == "div" and "section" in child["class"]
                ):
                    sections.append(child.extract())
        return "\n".join(str(s) for s in sections)

    def apply_banner_layout(html):
        html = _denest_sections(html)
        soup = bs(html, "html.parser")

        # Insert Bootstrap classes into section divs
        for s in soup.select("section,div.section"):
            h = s.find(["h1", "h2", "h3", "h4", "h5", "h6"])
            if not h:
                continue

            i = h.name[-1]

            h["class"] = [f"display-{i}"] + h.get("class", [])

            if h.name in ["h1", "h2"]:
                s.wrap(
                    soup.new_tag(
                        "div", **{"class": f"container-fluid sectionwrapper-{i}"}
                    )
                )
                s.wrap(soup.new_tag("div", **{"class": f"container section-{i}"}))

            if h.name == "h2":
                h.wrap(soup.new_tag("div", **{"class": "section-title-wrapper"}))
                h.wrap(soup.new_tag("div", **{"class": "section-title"}))

        # Process banner tags and modify section div styles
        for s in soup.find_all("banner"):
            image = s.get("image", None)
            color = s.get("color", None)
            caption = s.get("caption", None)

            d = s.find_parent("div", ["sectionwrapper-1", "sectionwrapper-2"])
            s.extract()
            if d is None:
                continue

            if image:
                image = copy_image(app, image)

            if image and color:
                style = (
                    f"background-image: linear-gradient({color},{color}), url({image});"
                )
            elif image:
                style = f"background-image: url({image});"
            elif color:
                style = f"background-color: {color};"
            else:
                style = None

            if style:
                d["style"] = style

            if caption:
                cd = soup.new_tag("div", **{"class": "section-banner-caption"})
                cd.string = caption
                d.append(cd)

        return str(soup)

    context["apply_banner_layout"] = apply_banner_layout


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
