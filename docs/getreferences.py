#!/usr/bin/env python
# -- Download Sphinx Book Theme reference docs --------------------------------
# These are the all of the reference docs used by the Sphinx Book Theme:
#   https://github.com/executablebooks/sphinx-book-theme
# To re-download, delete the `references\` folder and build the docs

import os
from pathlib import Path
import pprint

import click
import requests

PREFIX = "https://api.github.com/repos/executablebooks/sphinx-book-theme"
BRANCH = "master"


def download_files(repo_paths=["docs/references.bib", "docs/reference/"], local_path="reference"):
    if os.path.isdir(local_path):
        print("References already exist.  Skipping.")
        return

    files = []
    for repo_path in repo_paths:
        files.extend(find_files(repo_path=repo_path, path_is_file=repo_path[-1] != "/"))

    for path, rel_dir, url in files:
        final_path = Path(local_path) / Path(path).relative_to(rel_dir)
        os.makedirs(final_path.parent, exist_ok=True)
        if not final_path.exists():
            print(f"Downloading references file {path}")
            resp = requests.get(url)
            final_path.write_text(resp.content.decode())


def find_files(repo_path="docs/reference", path_is_file=False):
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
            rel_dir = os.path.dirname(repo_path) if path_is_file else repo_path
            files.append((item["path"], rel_dir, item["download_url"]))
        else:
            raise KeyError(f"Invalid response: {item}")
    return files


@click.command()
@click.argument("outdir", type=click.Path(), required=True)
def get_references(outdir):
    download_files(local_path=outdir)


if __name__ == "__main__":
    get_references()
