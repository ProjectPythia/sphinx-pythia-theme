import os
from pathlib import Path

from bs4 import BeautifulSoup as bs
import sass
from sphinx.application import Sphinx

__version__ = '0.0.2'
__dir__ = Path(__file__).parent


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(__dir__)
    return theme_path


def compile_scss(app, config):
    build_dir = Path(app.outdir)
    try:
        static_dir = app.config.html_static_path[0]
    except (AttributeError, IndexError):
        static_dir = ''
    source_dir = build_dir / static_dir / 'scss'
    source_fn = os.path.abspath(source_dir / 'pythia.scss')

    output_dir = build_dir / static_dir / 'css'
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    output_fn = os.path.abspath(output_dir / 'pythia.css')

    output_string = sass.compile(filename=source_fn)
    with open(output_fn, 'w') as f:
        f.write(output_string)


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

    def set_background(html, image_src=None, image_attr=None, overlay_clr=None):
        soup = bs(html, 'html.parser')

        if not image_src and not overlay_clr:
            return str(soup)

        image_url = context['pathto']('_static/' + image_src, 1) if image_src else None
        overlay = str(overlay_clr) if overlay_clr else None

        for div in soup.select('div.sectionwrapper-1'):
            if overlay and image_url:
                _style = f"background-image: linear-gradient({overlay}, {overlay}), url({image_url});"
            elif overlay:
                _style = f"background-color: {overlay};"
            else:
                _style = f"background-image: url({image_url});"
            div['style'] = _style

            if image_url and image_attr:
                span = soup.new_tag('span')
                span['class'] = ['background-attribution']
                span.string = str(image_attr)
                div.append(span)

        return str(soup)

    context['bootstrapify'] = bootstrapify
    context['denest_sections'] = denest_sections
    context['set_background'] = set_background


def setup(app: Sphinx):
    app.require_sphinx('3.5')
    app.add_html_theme('sphinx_pythia_theme', get_html_theme_path())
    app.connect('build-finished', compile_scss)
    app.connect('html-page-context', add_functions_to_context)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
