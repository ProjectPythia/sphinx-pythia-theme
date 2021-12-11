# About the Sphinx Pythia Theme

The Sphinx Pythia Theme is a [Sphinx Theme](https://www.sphinx-doc.org/en/master/usage/theming.html)
that inherits directly from the [Sphinx Book Theme](https://sphinx-book-theme.readthedocs.io/en/latest/)
used by the amazing [Jupyter Book project](https://jupyterbook.org/intro.html).  As a result, the
Sphinx Pythia Theme, through the Sphinx Book Theme, inherits from the awesome
[PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/),
which provides a great deal of functionality.

On top of all of these amazing themes, the Sphinx Pythia theme add a few simple changes.

## Domain Navigation

A *Domain Navigation* bar has been added to the top of every page.  The idea is that you can use
this theme for a collection of books or pages that each may have their own subdomain.  The Domain
Navigation bar is useful for making each site have a consistent look and feel.  As a consequence of
this new element on the page, the site logo has been moved from the left sidebar element into the
Domain Navigation bar.

The links on the Domain Navigation bar can be relative or absolute URLs, and the links are defined
in the `sphinx` &rarr; `config` &rarr; `html_theme_options` section of the Jupyter Book `_config.yml` file.  Alternatively, if using this theme with only Sphinx, and not using Jupyter Book, you can define the Domain Navigation links in the Sphinx `conf.py` file in the `html_theme_options` variable.

:::{tabbed} Sphinx

```python
html_theme = 'sphinx_pythia_theme'
html_theme_options = {
    'domnav': [
        {'content': 'Link1',
         'url': 'https://link1.com/some/link'},
        {'content': 'Link2',
         'url': 'https://link2.com/some/other/link'},
    ]
}
```

:::

:::{tabbed} Jupyter Book

```yaml
sphinx:
  config:
    html_theme: sphinx_pythia_theme
    html_theme_options:
      domnav:
        - content: Link1
          url: https://link1.com/some/link
        - content: Link2
          url: https://link2.com/some/other/link
```

:::

## Footer Bar

In addition to the Domain Navigation bar at the top of each page, a full-width footer
bar has been added to the bottom of every page.  By default, the footer bar only contains
copyright and additional information about the Sphinx version (if configured).  Two additional
sections can be added to the footer: a *logobar* and an *acknowledgement*.

The *logobar* section can be used to add logo images for various partner or collaboration
institutions, products, or other entities involved with site itself.  These are spread out
evenly across the footer in a light-gray full-width box.

To add logo images to the *logobar*, use the `logos` section of the `footer` `html_theme_options`.
The name given to each logo is used as the alternate name of the image in HTML.

:::{tabbed} Sphinx

```python
html_theme_options = {
    'footer': {
        'logos': {
            'name1': 'images/logo1.svg',
            'name2': 'images/logo2.svg',
        }
    }
}
```

:::

:::{tabbed} Jupyter Book

```yaml
sphinx:
  config:
    html_theme_options:
      footer:
        logos:
          name1: images/logo1.svg
          name2: images/logo2.svg
```

:::

The *acknowledgement* section of the footer can be used to give an acknowledgement or
disclaimer to your site.  If, for example, your site was funded by another party (or
parties), and you wish to acknowledge their contributions, you can add it easily in this
section.

To configure an *acknowledgement* section, you need simply add an `acknowledgement` section
to your `footer` `html_theme_options`.   The `content` is assumed to be a text acknowledgement,
and the `image` is an optional image associated with the acknowledgement (e.g., a logo for a
funding agency or similar).

:::{tabbed} Sphinx

```python
html_theme_options = {
    'footer': {
        'acknowledgement': {
            'content': 'Thanks to everyone who helped with this project!',
            'image': 'images/picture_of_everyone.png',
        }
    }
}
```

:::

:::{tabbed} Jupyter Book

```yaml
sphinx:
  config:
    html_theme_options:
      footer:
        acknowledgement:
          content: Thanks to everyone who helped with this project!
          image: images/picture_of_everyone.png
```

:::

## Banner Pages

An alternate layout for specific pages, called Banner pages, can be used with the Sphinx
Pythia Theme, too.  Banner pages are pages where each `H1` section (i.e., defined by a
`#` header) and `H2` section (i.e., defined by a `##` header) on the page is broken out
into its own full-width, well-padded element.  These elements allow you to attractively
layout *banner*-like sections on, for example, a landing page using the popular "one pager"
scrolling format.  (The [landing page](/index) for this documentation uses this layout.)

By default, `H1` sections (defined by `#` headers) are given a dark gray (Bootstrap's
`gray-700` color) background color with light text.  In contrast, `H2` sections (defined
by `##` headers) use dark text with alternating light-gray (Bootstrap's `light` and `gray-300`
colors) background colors.  All headings are given a Bootstrap
[`display`](https://getbootstrap.com/docs/4.0/content/typography/#display-headings)
CSS class and all paragraph text is given the Bootstrap
[`lead`](https://getbootstrap.com/docs/4.0/content/typography/#lead) CSS class.

Each *banner* section can be given its own background color or even background image.
To customize your own banners, all you need to do is add a `banner` directive to your
section.

::::{tabbed} reStructuredText

```rst
.. banner:
   color: rgba(40,40,60,0.8)
   image: images/pexels-jeff-stapleton-5792818.jpg
   caption: Photo by Jeff Stapleton from Pexels
```

::::

::::{tabbed} Myst Markdown

```markdown
:::{banner}
:color: rgba(40,40,60,0.8)
:image: images/pexels-jeff-stapleton-5792818.jpg
:caption: Photo by Jeff Stapleton from Pexels
:::
```

::::

The `color` option can be set to any valid CSS color value, including `rgba` values.
The `image` option can be set to any valid CSS image URL (local or remote), and the
`caption` option can be set to any string text.

If the `color` option is used by itself, then the given color will be used for the
*banner* section's `background-color` CSS style.  If the `image` option is used without
the `color` option, then the `background-image` CSS style for the section is set equal
to the the given value.  If both the `color` and `image` options are used, then the
`color` value will be used as an "overlay" on top of the given image, allowing you to
mute the background image as you see fit.

:::{warning}

If you do not use an `rgba` color with some level of transparency (the alpha component
of the `rgba` value), any background image you set will be hidden behind an opaque
overlay!  Use transparency appropriately.

:::
