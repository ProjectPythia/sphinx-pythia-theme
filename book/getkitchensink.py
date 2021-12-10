#!/usr/bin/env python
# -- Download kitchen sink reference docs -------------------------------------
# These are the kitchen sink files used by the Sphinx Themes gallery at
# https://github.com/sphinx-themes/sphinx-themes.org
# To re-download, delete the `references/kitchen-sink` folder and build the docs

import click
from pathlib import Path
from urllib import request

kitchen_sink_files = [
    "api.rst",
    "index.rst",
    "lists-and-tables.rst",
    "paragraph-markup.rst",
]


@click.command()
@click.argument("outdir", type=click.Path(), required=True)
def get_kitchen_sink_files(outdir):
    for ifile in kitchen_sink_files:
        path_file = Path(f"{outdir}/kitchen-sink/{ifile}")
        path_file.parent.mkdir(exist_ok=True)
        if not path_file.exists():
            print(f"Downloading kitchen sink file {ifile}")
            resp = request.urlopen(
                f"https://github.com/sphinx-themes/sphinx-themes.org/raw/master/sample-docs/kitchen-sink/{ifile}"  # noqa
            )
            header = ".. DOWNLOADED FROM sphinx-themes.org, DO NOT MANUALLY EDIT\n"
            path_file.write_text(header + resp.read().decode())


if __name__ == "__main__":
    get_kitchen_sink_files()
