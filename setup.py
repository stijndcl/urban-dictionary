import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent

dependencies = ["aiohttp==3.8.1", "click==8.1.3"]


def get_version():
    with open(here / "urban_dictionary/version.py") as fp:
        for line in fp:
            if line.startswith("__version__"):
                return line.split('"')[1]


setup(
    name="urban-dictionary",
    version=get_version(),
    description="CLI tool to get Urban Dictionary definitions",
    url="https://github.com/stijndcl/urban-dictionary",
    license="MIT",
    author="stijndcl",
    packages=[
        "urban_dictionary",
    ],
    python_requires=">=3.9",
    install_requires=dependencies,
    project_urls={
        "Bug Reports": "https://github.com/stijndcl/urban-dictionary/issues",
        "Source": "https://github.com/stijndcl/urban-dictionary",
    },
    entry_points={"console_scripts": ["urban-dictionary = urban_dictionary:main"]},
)
