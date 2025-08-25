# python-template

[![CI](https://github.com/todassy3/python-template/actions/workflows/ci.yml/badge.svg)](https://github.com/todassy3/python-template/actions/workflows/ci.yml)
[![Codecov](https://codecov.io/github/todassy3/python-template/graph/badge.svg?token=V17WX3DCH5)](https://codecov.io/github/todassy3/python-template)
[![Dependabot Updates](https://github.com/todassy3/python-template/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/todassy3/python-template/actions/workflows/dependabot/dependabot-updates)

## Install

```sh
$ pip install -e .
```

## Uninstall

```sh
$ pip uninstall python-template
```

## Usage

## Development

### Initialize

```sh
$ mise trust
$ mise install
$ pre-commit install
$ uv sync --frozen --all-groups
```

### Manage Dependencies

```sh
$ pre-commit autoupdate
$ uv add <pkg>
$ uv add <pkg> --dev
$ uv remove <pkg>
```

### Lint, Format and Test

```sh
$ pre-commit run --all-files
```
