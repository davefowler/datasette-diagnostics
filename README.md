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

![Diagnostics Datasette view](https://p38.f2.n0.cdn.getcloudapp.com/items/xQuOAD4k/56827593-a1a4-44a0-b98f-626ca17107bc.png?source=viewer&v=f2934ad2b3f1081ccc3ab70b064826da)

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-diagnostics
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
