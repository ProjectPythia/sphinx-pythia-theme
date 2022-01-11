About the Sphinx Pythia Theme
=============================

The Sphinx Pythia Theme is a `Sphinx Theme <https://www.sphinx-doc.org/en/master/usage/theming.html>`_
that inherits directly from the `Sphinx Book Theme <https://sphinx-book-theme.readthedocs.io/en/latest/>`_
used by the amazing `Jupyter Book project <https://jupyterbook.org/intro.html>`_.  As a result, the
Sphinx Pythia Theme, through the Sphinx Book Theme, inherits from the awesome
`PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/latest/>`_,
which provides a great deal of functionality.

On top of all of these amazing themes, the Sphinx Pythia theme add a few simple new features.

Top Navigation Bar
------------------

The Sphinx Pythia Theme brings back the fixed top navigation bar provided by the PyData Sphinx Theme.
Where the Sphinx Book Theme places your ``html_logo`` at the top of the left sidebar, the PyData Sphinx
Theme places the logo on the left of the top navigation bar.  The PyData Sphinx Theme allows the user
to set the link attached to the logo with the ``logo_link`` option in your Sphinx ``html_theme_options``
dictionary.  You can learn how to customize your logo on the
`PyData Sphinx Theme documentation <https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html#configure-project-logo>`_.

The links on the navigation bar can be set with the ``html_theme_options`` ``navbar_links`` option.
This is a list of dictionaries containing a ``name`` key, ``url`` key, and an ``external`` key.  The
``name`` key can be any string that you want to appear in the navbar.  The ``url`` key is a string
containing the URL that should be associated with the ``name`` in the navbar, and the ``external`` key
is a boolean indicating if the link is *external* or not.  (If *external*, an icon will be displayed
next to the ``name`` in the navbar indicating that clicking the link takes you away from the site).
Additionally, the
`external links <https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html#adding-external-links-to-your-nav-bar>`_
(``external_links``) option from the PyData Sphinx Theme still works, and these links
will be displayed after any links specified by the ``navbar_links`` option.

.. tabbed:: Sphinx

   .. code-block:: python

      html_theme = 'sphinx_pythia_theme'
      html_theme_options = {
          'navbar_links': [
              {'name': 'Link1',
               'url': 'https://link1.com/some/link',
               'external': True},
              {'name': 'Link2',
               'url': 'https://link2.com/some/other/link'},
          ]
      }

.. tabbed:: Jupyter Book

   .. code-block:: yaml

      sphinx:
        config:
          html_theme: sphinx_pythia_theme
          html_theme_options:
            navbar_links:
              - name: Link1
                url: https://link1.com/some/link
                external: True
              - content: Link2
                url: https://link2.com/some/other/link

.. note::

   The ``url`` value can be a Sphinx document name, in addition to an absolute or relative URL.  In fact,
   using Sphinx document names is the best way of generating the link correctly on different pages.

Icons can be displayed in the top right of the navigation bar using the PyData Sphinx Theme's
`icon links customization <https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html#local-image-icons>`_
(``icon_links``) option or by using the built-in PyData Sphinx Theme
`icon link shortcuts <https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html#icon-link-shortcuts>`_.

Footer Bar
----------

In addition to the top navigation bar at the top of each page, the full-width footer
bar from the PyData Sphinx Theme has been readded to the bottom of every page.  By default, the
footer bar only contains copyright and additional information about the Sphinx version (if configured).
Three additional sections can be added to the footer: a *logo bar*, a *bottom navigation menu*, and
an *extras* section.

Footer Logo Bar
^^^^^^^^^^^^^^^

The *logo bar* section can be used to add logo images for various partner or collaboration
institutions, products, or other entities involved with site itself.  These are spread out
evenly across the footer in a light-gray full-width box.

To add logo images to the *logo bar* in the footer, use the ``footer_logos`` option of the
``html_theme_options``.  The name given to each logo is used as the alternate name of
the image in HTML.

.. tabbed:: Sphinx

   .. code-block:: python

      html_theme_options = {
          'footer_logos': {
              'name1': 'images/logo1.svg',
              'name2': 'images/logo2.svg',
          }
      }

.. tabbed:: Jupyter Book

   .. code-block:: yaml

      sphinx:
        config:
          html_theme_options:
            footer_logos:
              name1: images/logo1.svg
              name2: images/logo2.svg

Footer Navigation Menu
^^^^^^^^^^^^^^^^^^^^^^

The *bottom navigation bar* section of the footer is placed directly above the *info* bar (containing
the copyright information, author, last updated, and Sphinx version).  The contents of the *bottom
navigation bar* can be set with the ``footer_menu`` option of the ``html_theme_options``.  This option
defines a list of *columns* with *titles* and unstyled lists of links or text below each title.  Each
column is a dictionary with a ``title`` key containing text for the title of the column, a ``class``
key containing any CSS classes to add to the HTML column division, and an ``items`` key containing a
list of dictionaries containing ``name``, ``url``, and ``external`` keys (with the same meaning as
the keys in the ``navbar_links`` option above).

.. tabbed:: Sphinx

   .. code-block:: python

      html_theme_options = {
          'footer_menu': [
              {
                  'title': 'Column A',
                  'class': 'col-8 col-sm-4 col-md-3 col-lg-2',
                  'items': [
                      {
                          'name': 'Link 1',
                          'url': '#local-link-1',
                      },
                      {
                          'name': 'Link 2',
                          'url': 'https://external.link/2',
                          'external': True,
                      },
                  ],
              },
              {
                  'title': 'Column B',
                  'class': 'col-8 col-sm-4 col-md-3 col-lg-2',
                  'items': [
                      {
                          'name': 'Link 3',
                          'url': '#local-link-3',
                      },
                      {
                          'name': 'Link 4',
                          'url': 'https://external.link/4',
                          'external': True,
                      },
                  ],
              },
          ],
      }

.. tabbed:: Jupyter Book

   .. code-block:: yaml

      sphinx:
        config:
          html_theme_options:
            footer_menu:
              - title: Column A
                class: col-8 col-sm-4 col-md-3 col-lg-2
                items:
                  - name: Link 1
                    url: '#local-link-1'
                  - name: Link 2
                    url: https://external.link/2
                    external: True
              - title: Column B
                class: col-8 col-sm-4 col-md-3 col-lg-2
                items:
                  - name: Link 3
                    url: '#local-link-3'
                  - name: Link 4
                    url: https://external.link/4
                    external: True

Extra Footer
^^^^^^^^^^^^

The *extra* section of the footer is displayed immediately below the *info* section, and
it can be set with the
`extra footer <https://sphinx-book-theme.readthedocs.io/en/latest/customize/index.html?highlight=extra_footer#theme-options>`_
(``extra_footer``) Sphinx Book Theme option.

Special Page layouts
--------------------

The Sphinx Pythia Theme comes with two special layouts for pages: the *banner* layout, and the
*standalone* layout.

Banner Pages
^^^^^^^^^^^^

An alternate layout for specific pages, called Banner pages, can be used with the Sphinx
Pythia Theme, too.  Banner pages are pages where each ``H1`` section (i.e., defined by a
``#`` header in markdown) and ``H2`` section (i.e., defined by a ``##`` header in markdown)
on the page is broken out into its own full-width, well-padded element.  These elements
allow you to attractively layout *banner*-like sections on, for example, a landing page
using the popular "one pager" scrolling format.  (The :doc:`/index` page of this
documentation uses this layout.)

By default, ``H1`` sections (defined by ``#`` headers in markdown) are given a dark gray
(Bootstrap's ``gray-700`` color) background color with light text.  In contrast, ``H2``
sections (defined by ``##`` headers in markdown) use dark text with alternating light-gray
(Bootstrap's ``light`` and ``gray-300`` colors) background colors.  All headings are
given a Bootstrap
`display <https://getbootstrap.com/docs/4.0/content/typography/#display-headings>`_
CSS class and all paragraph text is given the Bootstrap
`lead <https://getbootstrap.com/docs/4.0/content/typography/#lead>`_ CSS class.

Each *banner* section can be given its own background color or even background image.
To customize your own banners, all you need to do is add a ``banner`` directive to your
section.

.. tabbed:: reStructuredText

   .. code-block:: rst

      .. banner:
        color: rgba(40,40,60,0.8)
        image: images/pexels-jeff-stapleton-5792818.jpg
        caption: Photo by Jeff Stapleton from Pexels
        class: dark-banner

.. tabbed:: Myst Markdown

   .. code-block:: markdown

      :::{banner}
      :color: rgba(40,40,60,0.8)
      :image: images/pexels-jeff-stapleton-5792818.jpg
      :caption: Photo by Jeff Stapleton from Pexels
      :class: dark-banner
      :::

The ``color`` option can be set to any valid CSS color value, including ``rgba`` values.
The ``image`` option can be set to any valid CSS image URL (local or remote), and the
``caption`` option can be set to any string text.

If the ``color`` option is used by itself, then the given color will be used for the
*banner* section's ``background-color`` CSS style.  If the ``image`` option is used without
the ``color`` option, then the ``background-image`` CSS style for the section is set equal
to the the given value.  If both the ``color`` and ``image`` options are used, then the
``color`` value will be used as an "overlay" on top of the given image, allowing you to
mute the background image as you see fit.

.. warning::

   If you do not use an ``rgba`` color with some level of transparency (the alpha component
   of the ``rgba`` value), any background image you set will be hidden behind an opaque
   overlay!  Use transparency appropriately.

Additional CSS styling can be given to the *banner* HTML element with the ``class`` option
of the ``banner`` directive.  The built-in ``dark-banner`` class changes the text color to
work well with dark background banners, but you can define your own CSS class for these sections
yourself.

Because *banner* pages require significant changes to the default Sphinx/Docutils layout,
you need to declare which pages (by document name) will have the *banner* layout.  To do
this, you need to declare the ``page_layouts`` option in the ``html_theme_options`` and
tell the theme to use the ``page-banner.html`` template.

.. tabbed:: Sphinx

   .. code-block:: python

      html_theme_options = {
          'page_layouts': {
              'index': 'page-banner.html',
          }
      }

.. tabbed:: Jupyter Book

   .. code-block:: yaml

      sphinx:
        config:
          html_theme_options:
            page_layouts:
              index: page-banner.html

The key (e.g., ``index`` in the above example) indicates the page name, and the value
(e.g., ``page-banner.html`` in the above example) indicates the page layout template
to use for the given document name.  By default, any pages not listed in the
``page_layouts`` option will have the default page layout, which corresponds to
the typical layout of any Jupyter Book page.

Standalone Pages
^^^^^^^^^^^^^^^^

Standalone pages use the ``page-standalone.html`` template in the same way that the
*banner* pages above use the ``page-banner.html`` template.  Standalone pages have
the same heading and text styling used by banner pages, but they do not have extra
padding nor the ability to declare banner backgrounds to the sections.  The
:doc:`/standalone` page is an example of this layout.

Custom Templates
----------------

The Sphinx Pythia Theme uses certain custom templates to define how the content in certain
sections of the page will display.  For the links in the top navigation bar, the ``navbar-menu.html``
template is used.  For how to define *banner* and *standalone* page layouts, the ``page-banner.html``
and the ``page-standalone.html`` templates are used.  For footer content, the ``footer-logos.html``,
``footer-info.html``, ``footer-menu.html``, and the ``footer-extra.html`` templates are used.

Anyone can override these templates by putting their own versions of these templates (i.e.,
using the same template filenames) in a ``_templates`` directory within their Sphinx or Jupyter
Book source (at the same level as their ``conf.py`` or ``_config.yml`` files).
