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
    files = find_files(repo_path=repo_path)

    for path, url in files:
        if path == repo_path:
            rel_path = Path(path).name
        else:
            rel_path = Path(path).relative_to(repo_path)
        final_path = Path(local_path) / rel_path
        print(path, repo_path, local_path, final_path)
        os.makedirs(final_path.parent, exist_ok=True)
        if not final_path.exists():
            print(f"Downloading references file {path}")
            resp = requests.get(url)
            final_path.write_text(resp.content.decode())


def find_files(repo_path="docs/reference"):
    url = f"{PREFIX}/contents/{repo_path}?ref={BRANCH}"
    resp = requests.get(url)
    resp_json = resp.json()
    if isinstance(resp_json, dict):
        resp_json = [resp_json]

    files = []
    for item in resp_json:
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
    if os.path.isdir(outdir):
        print("References already exist.  Skipping.")
        return

    download_files(repo_path="docs/reference", local_path=outdir)
    download_files(repo_path="docs/references.bib", local_path=outdir)


if __name__ == "__main__":
    get_references()
