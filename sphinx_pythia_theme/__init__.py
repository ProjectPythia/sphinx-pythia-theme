import os
from pathlib import Path

from bs4 import BeautifulSoup as bs
from bs4.element import NavigableString
from sphinx.application import Sphinx

__version__ = "0.0.1"


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(Path(__file__).parent)
    return theme_path


def add_functions_to_context(app, pagename, templatename, context, doctree):

    def find_tags_by_name(node, name, maxdepth=None, _depth=0):
        found_tags = []
        if node.name == name:
            found_tags.append(node)
        maxdepth_not_exceeded = True if not maxdepth else _depth <= maxdepth
        if hasattr(node, 'children') and maxdepth_not_exceeded:
            for child in node.children:
                found_tags += find_tags_by_name(child, name, maxdepth=maxdepth, _depth=_depth+1)
        return found_tags


    def generate_page_nav_items():
        toc = context.get('toc')
        if not toc:
            return []

        soup = bs(toc, 'html.parser')
        list_items = find_tags_by_name(soup, 'li', maxdepth=3)
        for li in list_items:
            for ul in li.find_all('ul'):
                ul.extract()
            li['class'] = ['nav-item'] + li.get('class', [])
            anchor = li.find('a')
            if anchor:
                anchor['class'] = ['nav-link'] + anchor.get('class', [])
                if anchor['href'] == '#':
                    anchor.string.replace_with('Home')

        return [str(li).replace('\n', '').strip() for li in list_items]


    def generate_body_sections():
        body = context.get('body')
        if not body:
            return []

        soup = bs(body, 'html.parser')
        divisions = find_tags_by_name(soup, 'div')

        sections = []
        for div in divisions:
            for _div in div.find_all('div'):
                _div.extract()

            h = div.find(['h1', 'h2'])
            if not h:
                continue

            kind = 'banner' if h.name == 'h1' else 'section'
            title = h.extract()
            title_link = title.find('a')
            if title_link:
                section_id = title_link['href'].replace('#', '')
                link_icon = soup.new_tag('i')
                link_icon['class'] = ['bi', 'bi-link']
                title_link.string.replace_with(link_icon)
            else:
                section_id = None

            section = {}
            section['kind'] = kind
            section['title'] = str(title)
            section['id'] = section_id
            section['text'] = ''.join(str(c).strip() for c in div.contents)

            sections.append(section)

        return sections

    context['generate_page_nav_items'] = generate_page_nav_items
    context['generate_body_sections'] = generate_body_sections


def setup(app: Sphinx):
    app.add_html_theme('sphinx_pythia_theme', get_html_theme_path())
    app.connect("html-page-context", add_functions_to_context)
