import os
import itertools
from pathlib import Path

from bs4 import BeautifulSoup as bs
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

    def get_nav_items():
        toc = context.get('toc')
        if not toc:
            return []

        soup = bs(toc, 'html.parser')
        nav_items = find_tags_by_name(soup, 'li', maxdepth=3)
        for li in nav_items:
            for ul in li.find_all('ul'):
                ul.extract()
            li['class'] = ['nav-item'] + li.get('class', [])
            anchor = li.find('a')
            if anchor:
                anchor['class'] = ['nav-link'] + anchor.get('class', [])

        return [str(li).replace('\n', '').strip() for li in nav_items]

    def get_sidebar_items():
        toctree = context['toctree'](maxdepth=-1, collapse=False, includehidden=True)
        if not toctree:
            return []

        soup = bs(toctree, 'html.parser')

        sidebar_items = []
        for li in soup.find_all('li', class_="toctree-l1"):
            a = li.find('a').extract()
            ul = li.find('ul')
            if ul:
                ul = ul.extract()

                ul['class'] = 'list-unstyled'
                for _ul in ul.find_all('ul'):
                    _ul['class'] = 'list-unstyled'

                for _a in ul.find_all('a'):
                    # _a['class'] = ['btn', 'btn-sm'] + _a.get('class', [])
                    _a['class'] = ['btn', 'btn-sm']

                for _li in ul.find_all('li'):
                    _li.attrs = {}

            else:
                ul = ''

            sidebar_item = {}
            sidebar_item['title'] = a.string
            sidebar_item['href'] = a['href']
            sidebar_item['id'] = a['href'].replace('#', '')
            sidebar_item['is_current'] = 'current' in li['class']
            sidebar_item['contents'] = str(ul)

            sidebar_items.append(sidebar_item)

        return sidebar_items

    def get_onepage_body_sections():
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

    context['get_nav_items'] = get_nav_items
    context['get_sidebar_items'] = get_sidebar_items
    context['get_onepage_body_sections'] = get_onepage_body_sections


def set_default_permalinks_icon(app):
    if 'permalinks_icon' in app.config.html_theme_options:
        icon_class = app.config.html_theme_options['permalinks_icon']
    else:
        icon_class = 'bi bi-link'
    app.config.html_permalinks_icon = f'<i class="{icon_class}"></i>'


def setup(app: Sphinx):
    app.require_sphinx('3.5')
    app.add_html_theme('sphinx_pythia_theme', get_html_theme_path())
    app.connect('builder-inited', set_default_permalinks_icon)
    app.connect('html-page-context', add_functions_to_context)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
