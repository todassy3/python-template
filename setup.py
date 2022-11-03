"""setup"""
from __future__ import annotations

import re
import subprocess

from setuptools import find_packages, setup


def read_file(file: str) -> str:
    """Read a file"""
    with open(file, encoding="utf-8") as fin:
        content = fin.read()
    return content


def get_version(file: str) -> str:
    """Get package version"""
    pattern = r"^__version__ = ['\"]([^'\"]*)['\"]"
    content = read_file(file)
    match = re.search(pattern, content, re.M)
    if match is None:
        raise RuntimeError("Could not find version the file '_version.py'")

    major, minor = match.groups()[0].split(".", 1)

    try:
        cmd = ["git", "rev-list", "HEAD"]
        proc = subprocess.run(cmd, text=True, check=True, capture_output=True)
        git_rev_list = proc.stdout.splitlines()
        revision = len(git_rev_list)
    except subprocess.CalledProcessError:
        revision = 0

    version = ".".join([major, minor, str(revision)])
    return version


setup(
    name="mypackage",
    version=get_version("mypackage/_version.py"),
    author="todahiroki",
    author_email="todahiroki3@gmail.com",
    maintainer="todahiroki",
    maintainer_email="todahiroki3@gmail.com",
    url="https://github.com/todassy/python-package-template",
    description="Python package template.",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    # package_data={"": ["*.yaml"]},
    # install_requires=["requests", "types-requests"],
    tests_require=["pytest", "pytest-cov", "pytest-randomly"],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["mypackage = mypackage.cli:_main"]},
)
