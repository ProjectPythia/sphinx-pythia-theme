from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="sphinx-pythia-theme",
    url="https://sphinx-pythia-theme.readthedocs.io",
    project_urls={
        "Documentation": "https://projectpythia.org",
        "Source Code": "https://github.com/ProjectPythia/sphinx-pythia-theme",
        "Bug Tracker": "https://github.com/ProjectPythia/sphinx-pythia-theme/issues",
    },
    author="Kevin Paul",
    author_email="kpaul@ucar.edu",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ],
    license="Apache 2.0",
    description="The Sphinx Pythia Theme",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    keywords="sphinx, theme, jupyter, notebook",
    zip_safe=True,
    include_package_data=True,
    install_requires=[
        "sphinx-book-theme>=0.1.7",
    ],
    packages=find_packages(),
    entry_points={"sphinx.html_themes": ["sphinx_pythia_theme = sphinx_pythia_theme"]},
    use_scm_version={"version_scheme": "post-release", "local_scheme": "dirty-tag"},
)
