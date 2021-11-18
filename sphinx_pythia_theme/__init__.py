from bs4 import BeautifulSoup as bs
from sphinx.application import Sphinx

from .banner import Banner

__version__ = "0.1.0"


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

            d = s.find_parent("div", ["sectionwrapper-1", "sectionwrapper-2"])
            s.extract()
            if d is None:
                continue

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

        return str(soup)

    context["apply_banner_layout"] = apply_banner_layout


def setup(app: Sphinx):
    app.require_sphinx("3.5")
    app.add_directive("banner", Banner)
    app.connect("html-page-context", add_functions_to_context)

    return {
        "version": "0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
