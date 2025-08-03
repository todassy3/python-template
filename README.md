# python-template

[![CI](https://github.com/todassy3/python-template/actions/workflows/ci.yml/badge.svg)](https://github.com/todassy3/python-template/actions/workflows/ci.yml)
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
$ pre-commit autoupdate
$ uv sync --frozen --all-groups
```

### Manage Dependencies

```sh
$ uv add <pkg>
$ uv add <pkg> --dev
$ uv remove <pkg>
```

### Test

```sh
$ pytest
$ pre-commit run --all-files
```
