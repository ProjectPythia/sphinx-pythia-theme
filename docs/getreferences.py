#!/usr/bin/env python
# -- Download Sphinx Book Theme reference docs --------------------------------
# These are the all of the reference docs used by the Sphinx Book Theme:
#   https://github.com/executablebooks/sphinx-book-theme
# To re-download, delete the `references\` folder and build the docs

import os
from pathlib import Path

import click
import requests

PREFIX = "https://api.github.com/repos/executablebooks/sphinx-book-theme"
BRANCH = "master"


def download_files(repo_path="docs/reference", local_path="reference"):
    if os.path.isdir(local_path):
        print("References already exist.  Skipping.")
        return

    files = find_files(repo_path=repo_path)
    for path, url in files:
        final_path = Path(local_path) / Path(path).relative_to(repo_path)
        os.makedirs(final_path.parent, exist_ok=True)
        if not final_path.exists():
            print(f"Downloading references file {path}")
            resp = requests.get(url)
            final_path.write_text(resp.content.decode())


def find_files(repo_path="docs/reference"):
    url = f"{PREFIX}/contents/{repo_path}?ref={BRANCH}"
    resp = requests.get(url)
    files = []
    for item in resp.json():
        if item["type"] == "dir":
            files.extend(find_files(repo_path=item["path"]))
        elif item["download_url"]:
            files.append((item["path"], item["download_url"]))
        else:
            raise KeyError(f"Invalid response: {item}")
    return files


@click.command()
@click.argument("outdir", type=click.Path(), required=True)
def get_references(outdir):
    download_files(local_path=outdir)


if __name__ == "__main__":
    get_references()
