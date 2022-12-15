from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-diagnostics",
    description="Run diagnostics on query results",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Dave Fowler",
    url="https://github.com/davefowler/datasette-diagnostics",
    project_urls={
        "Issues": "https://github.com/davefowler/datasette-diagnostics/issues",
        "CI": "https://github.com/davefowler/datasette-diagnostics/actions",
        "Changelog": "https://github.com/davefowler/datasette-diagnostics/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_diagnostics"],
    entry_points={"datasette": ["diagnostics = datasette_diagnostics"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    package_data={
        "datasette_diagnostics": ["templates/*"]
    },
    python_requires=">=3.7",
)
