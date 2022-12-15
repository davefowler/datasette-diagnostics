# datasette-diagnostics

[![PyPI](https://img.shields.io/pypi/v/datasette-diagnostics.svg)](https://pypi.org/project/datasette-diagnostics/)
[![Changelog](https://img.shields.io/github/v/release/davefowler/datasette-diagnostics?include_prereleases&label=changelog)](https://github.com/davefowler/datasette-diagnostics/releases)
[![Tests](https://github.com/davefowler/datasette-diagnostics/workflows/Test/badge.svg)](https://github.com/davefowler/datasette-diagnostics/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/davefowler/datasette-diagnostics/blob/main/LICENSE)

!WARNING - heavy Work In Progress

Run diagnostics on query results in Datasette.

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-diagnostics

## Usage

When you view a table or run a query you'll see a "diagnostics" option in the export ("This data as") menu

![Diagnostics Datasette view](https://p38.f2.n0.cdn.getcloudapp.com/items/JruygbWq/2b1c9dd9-a342-48b3-ad5f-42533371b4ff.png?source=viewer&v=8ff4ea38a9209c681e3465d87457dafa)

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-diagnostics
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
