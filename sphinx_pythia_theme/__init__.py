import os
from pathlib import Path

from bs4 import BeautifulSoup as bs
from sphinx.application import Sphinx

__version__ = '0.0.2'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(Path(__file__).parent)
    return theme_path


def add_functions_to_context(app, pagename, templatename, context, doctree):
    def denest_sections(html):
        soup = bs(html, 'html.parser')

        sections = []
        for h1 in soup.find_all(['h1']):
            sections.append(h1.parent)
            for child in h1.parent.children:
                if (child.name == 'section') or (child.name == 'div' and 'section' in child['class']):
                    sections.append(child.extract())

        return '\n'.join(str(s) for s in sections)

    def bootstrapify(html):
        soup = bs(html, 'html.parser')

        for s in soup.select('section,div.section'):
            h = s.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if not h:
                continue

            i = h.name[-1]

            h['class'] = [f'display-{i}'] + h.get('class', [])

            if h.name in ['h1', 'h2']:
                s.wrap(soup.new_tag('div', **{'class': f'container-fluid sectionwrapper-{i}'}))
                s.wrap(soup.new_tag('div', **{'class': f'container section-{i}'}))

            if h.name == 'h2':
                h.wrap(soup.new_tag('div', **{'class': 'section-title-wrapper'}))
                h.wrap(soup.new_tag('div', **{'class': 'section-title'}))

        return str(soup)

    def insert_background_images(html, img_src):
        soup = bs(html, 'html.parser')

        for div in soup.select('div.sectionwrapper-1'):
            div['style'] = f"background-image: linear-gradient(rgba(26, 100, 143, 0.85), rgba(26, 100, 143, 0.85)), url({img_src});"

        return str(soup)

    context['insert_background_images'] = insert_background_images
    context['bootstrapify'] = bootstrapify
    context['denest_sections'] = denest_sections


def setup(app: Sphinx):
    app.require_sphinx('3.5')
    app.add_html_theme('sphinx_pythia_theme', get_html_theme_path())
    app.connect('html-page-context', add_functions_to_context)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
