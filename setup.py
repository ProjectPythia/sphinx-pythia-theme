from setuptools import setup, find_packages
from pathlib import Path


lines = Path("sphinx_pythia_theme").joinpath("__init__.py")
for line in lines.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break


setup(
    name="sphinx-pythia-theme",
    version=version,
    description="Sphinx Pythia Theme",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    url="https://github.com/ProjectPythia/sphinx-pythia-theme",
    project_urls={
        "Documentation": "https://projectpythia.org",
        "Source": "https://github.com/ProjectPythia/sphinx-pythia-theme",
        "Tracker": "https://github.com/ProjectPythia/sphinx-pythia-theme/issues",
    },
    author="Kevin Paul",
    author_email="kpaul@ucar.edu",
    keywords="reproducible science environments scholarship notebook",
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
    install_requires=[
        "sphinx-book-theme>=0.1.7",
    ],
    entry_points={
        "sphinx.html_themes": [
            "sphinx_pythia_theme = sphinx_pythia_theme",
        ]
    },
    packages=find_packages(),
    include_package_data=True,
)
