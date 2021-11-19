from docutils import nodes
from docutils.parsers.rst import directives, Directive


class Banner(Directive):
    """
    A Banner directive for use with Banner Pages

    The Banner directive adds a <banner ... /> HTML tag to the HTML output
    of the page.  At construction time of the HTML page with Sphinx, the <banner/>
    tag itself will be removed from the HTML and the attributes of the <banner/>
    tag will be used to set the parent section-wrapper div's `background-image` or
    `background-color` CSS properties, as appropriate.

    If only the `image` option is set, then the parent section-wrapper div's
    `background-image` CSS property will be set to:

        background-image: url(`image`);

    where `image` is the option set in the <banner/> tag's `image` attribute.

    If only the `color` option is set, then the parent section-wrapper div's
    `background-color` CSS property will be set to:

        background-color: `color`;

    where `color` is the option set in the <banner/> tag's `color` attribute.

    If both the `image` and `color` options are set, then the parent section-wrapper
    div's `background-image` CSS property will be set to:

        background-image: linear-gradient(`color`, `color`), url(`image`);

    where `color` is the option set in the <banner/> tag's `color` attribute, and
    `image` is the option set in the <banner/> tag's `image` attribute.

    The `caption` option specified a text caption to be displayed at the
    bottom right of the banner element.
    """

    option_spec = {
        "image": directives.uri,
        "color": directives.unchanged,
        "caption": directives.unchanged,
    }

    def run(self):
        if not self.state.document.settings.raw_enabled:
            raise self.warning('"%s" directive disabled.' % self.name)
        options = " ".join(f'{str(k)}="{str(v)}"' for k, v in self.options.items())
        text = f"<banner {options} />"
        attributes = {"format": "html"}
        node = nodes.raw("", text, **attributes)
        return [node]
