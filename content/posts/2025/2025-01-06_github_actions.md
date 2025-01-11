+++
title = 'Setting up OpenWeather Report GitHub Actions'
date = 2025-01-06T19:50:52-06:00
draft = false
tags = ['python','openweather_report','github actions','uv','astral']
summary = 'Adding GitHub workflows to help with linting, testing and publishing.'
comments = true
+++

## Overview

[OpenWeather Report](https://github.com/cetyler/openweather_report) I did my
initial release in 2023.
Before I start adding more features, I wanted to create some tooling to help
with linting, testing and publishing.
Using what I learn from
[Real Python's article](https://realpython.com/github-actions-python/)
on continuous integration and some other sites in creating my own workflows.

## CI/CD

In the past, I used helper scripts and [pre-commit](https://pre-commit.com) to
semi-automate linting, testing and publishing.
Continuous Integration (CI) and Continuous Deployment (CD) makes it possible to
have this process fully automated.
Using GitHub Actions, makes this possible at the repository level instead of the
developer PC to make the tooling consistent.

For OpenWeather Report, I am the only developer and don't anticipate getting an
additional developers in the near future.
However, I would like to understand how these tools work.
Keep in mind that [Gitea](https://about.gitea.com), [GitLab](https://gitlab.com)
and I am sure others also have something similar to GitHub Actions. 

## Linting

The nice thing about using GitHub Actions, you can separate functions into
separate files.
Linting is something that I want to happen every time there is a commit at
either the `main` branch or any `feature` branch.
I ended up using [uv](https://docs.astral.sh/uv/) to install dependencies and
to run [ruff](https://astral.sh/ruff).

```toml
name: Lint Python Code

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
          cache-dependency-glob: "uv.lock"
      - uses: actions/setup-python@v5
        with:
          python-version-file: 'pyproject.toml' 

      - name: Install dependencies
        run: uv sync --all-extras --dev
      - name: Run Ruff
        run: uvx ruff check --output-format=github
      - name: Run mypy
        run: uvx mypy -m openweather_report --strict 
```

This file is placed in `.github/workflows/lint.yml`.
For my purposes running on Ubuntu is fine though GitHub does have other options.
Finally, I use [mypy](https://www.mypy-lang.org) to do some static type
checking.

## Testing

Something I wanted to try is testing multiple versions of Python.
Not really required for this project but I would like **how** to do it before I
**need** to do it.

```toml
name: Run Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_call:
  workflow_dispatch:

jobs:
  testing:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]

    steps:
      - uses: actions/checkout@v4
      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
          python-version: ${{ matrix.python-version }}
      - name: Setup python
        run: uv python install
      - name: Install dependencies
        run: uv sync --all-extras --dev
      - name: Run Pytest
        run: pytest tests
```

This file is placed `.github/workflow/testing.yml`.
For this project will support Python 3.11 through 3.12.
Again using `uv` to install Python and setup dependencies.
Finally [pytest](https://docs.pytest.org/en/stable/) to perform the tests.
Notice the line `python-version: ${{ matrix.ptyhon-version }}` is where the
Python version goes from `python-version: ["3.11, "3.12", "3.13"]`.

## Publishing

This program does get packaged and published on
[PyPi](https://pypi.org/project/openweather_report/).
I also want to create a release on
[GitHub](https://github.com/cetyler/openweather_report/releases/).
Unlike the previous workflows, I only want this to run when a tag is applied.

```toml
name: Publish to PyPI
on:
  push:
    tags:
      - '*.*.*'

jobs:
  publish:
    runs-on: ubuntu-latest
    environment: pypi
    permissions:
      id-token: write
      contents: write 
    steps:
      - uses: actions/checkout@v4
      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
          cache-dependency-glob: "uv.lock"

      - name: Setup Python
        run: uv python install
      - name: Install dependencies
        run: uv sync --all-extras
      - name: Build package
        run: uv build
      - name: Publish package
        run: uv publish

      - name: Create GitHub Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh release create ${{ github.ref_name }} --title "Release ${{ github.ref_name  }}" -F RELEASE_NOTES.md
```

This file is placed `.github/workflow/publish.yml`.
The format looks similar to the previous workflow except at the top where when
a tag is pushed is the only time this workflow will run.
In order to publish to PyPi, I followed the instructions at
[Publishing](https://pypi.org/manage/account/publishing/) for GitHub.
Then I use `uv` install Python and dependencies like before but use `uv` to
build and publish the package.

It took a little bit more work to create a GitHub release.
I started with an article by
[Neo](https://dev.to/hanaosan/github-actions-automate-build-and-deployment-of-your-python-package-to-pypi-and-github-releases-51hj)
as well as the
[Real Python](https://realpython.com/github-actions-python/#publishing-your-package-automatically-to-pypi)
and got close but did not like how the release notes looked.
Also I was having trouble attempting to put the Python package on GitHub.
In the future I would like to include the Python package but for now will do the
following:

- Create a `RELEASE_NOTES.md` and manually edit for that particular release.
- Use [gh](https://cli.github.com) to create the release.
- For now the release will just be a `zip`/`tarball`.

## Security

Similar to testing multiple Python versions, for this project I don't really
need do security and dependency updates but I would like to learn how to do it.

```toml
---
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"


  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

This file is located `.github/dependabot.yml`.
This will check my dependencies for my project as well as the other GitHub
Actions.

## Conclusion

For the most part, it was straight-forward to setup and verify that my
GitHub Actions works.
For work I will need to use
[Azure Pipelines](https://azure.microsoft.com/en-us/products/devops/pipelines).
I do have [Gitea](https://about.gitea.com) self hosted instance and would like
to be able to do the same thing except not publishing to PyPi but on my own
private PyPi repository.
Learning how to do GitHub Actions will help with my current projects and
extend to my career.
