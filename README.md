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

![Diagnostics Datasette view](https://p38.f2.n0.cdn.getcloudapp.com/items/d5uypvkB/d1a41287-7b52-4825-a33d-f2f074274600.jpg?source=viewer&v=1e43b1d2fc73306b021588c208dfe568)

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-diagnostics
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
