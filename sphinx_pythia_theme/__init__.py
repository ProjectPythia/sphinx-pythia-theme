import os
import itertools
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


    def generate_page_nav_items(includehome=True):
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

        if list_items and includehome:
            top_li = list_items[0]
            anchor = top_li.find('a')
            if anchor['href'] == '#':
                anchor.string.replace_with('Home')

        return [str(li).replace('\n', '').strip() for li in list_items]


    def generate_doc_nav_items(includehome=True, **kwargs):
        toctree = context['toctree'](**kwargs)
        if not toctree:
            return []

        soup = bs(toctree, 'html.parser')

        list_items = []

        if includehome:
            li = soup.new_tag('li')
            li['class'] = ['toctree-l1']
            anchor = soup.new_tag('a')
            anchor['class'] = ['reference', 'internal']
            anchor['href'] = '#'
            anchor.string = 'Home'
            li.append(anchor)
            list_items = [li]

        list_items += find_tags_by_name(soup, 'li', maxdepth=3)
        for li in list_items:
            for ul in li.find_all('ul'):
                ul.extract()
            li['class'] = ['nav-item'] + li.get('class', [])
            anchor = li.find('a')
            if anchor:
                anchor['class'] = ['nav-link'] + anchor.get('class', [])

        return [str(li).replace('\n', '').strip() for li in list_items]


    def generate_body_sections():
        body = context.get('body')
        if not body:
            return []

        soup = bs(body, 'html.parser')

        divisions = []
        for h1 in soup.find_all(['h1']):
            divisions.append(h1.parent)
            for child in h1.parent.children:
                if child.name == 'div':
                    divisions.append(child.extract())

        sections = []
        section_classes = [
            'section-box-light',
            'section-box-light-gray',
            'section-box-dark-gray',
            'section-box-light-gray',
        ]
        itr = itertools.cycle(section_classes)
        for div in divisions:
            h = div.find(['h1', 'h2'])
            if not h:
                continue

            if h.name == 'h1':
                kind = 'banner'
                hclass = 'display-1'
                for p in div.find_all('p'):
                    p['class'] = ['lead'] + p.get('class', [])
            else:
                kind = 'section'
                hclass = 'display-5'
            title = h.extract()
            title['class'] = [hclass] + title.get('class', [])
            title_link = title.find('a')
            section_id = title_link['href'].replace('#', '')

            section = {}
            section['kind'] = kind
            section['title'] = str(title)
            section['id'] = section_id
            section['class'] = None if kind == 'banner' else next(itr)
            section['contents'] = ''.join(str(c).strip() for c in div.contents)

            sections.append(section)

        return sections

    context['generate_page_nav_items'] = generate_page_nav_items
    context['generate_doc_nav_items'] = generate_doc_nav_items
    context['generate_body_sections'] = generate_body_sections


def set_default_permalinks_icon(app):
    if 'permalinks_icon' in app.config.html_theme_options:
        app.config.html_permalinks_icon = app.config.html_theme_options['permalinks_icon']
    else:
        app.config.html_permalinks_icon = '<i class="bi bi-link"></i>'


def setup(app: Sphinx):
    app.require_sphinx('3.5')
    app.add_html_theme('sphinx_pythia_theme', get_html_theme_path())
    app.connect('builder-inited', set_default_permalinks_icon)
    app.connect('html-page-context', add_functions_to_context)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
