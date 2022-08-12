Title: Calculator Project -- Setup
Date: 2022-01-22 15:00
Category: Python
Tags: python, project, library, package
Author: Christopher
Summary: Initial setup of the calculator project.
comment_id: calculator_setup
Status: published
series: Calculator Project
series_index: 2

## Overview

From the [previous article]({filename}/python/2022-01-15-calculator_project.md),
the plan is to create [calculator](https://github.com/cetyler/calculator) in
order to update my Python workflow.
This article will cover setting up the project.

## Initial Cookiecutter

At the end of the project, I plan on creating a my own
[Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) template.
Initially I will use
[Audrey's](https://github.com/audreyfeldroy/cookiecutter-pypackage).
Answer the following questions:

- Name
- Email
- Github username
- Project Name
- Project description
- PyPi username
  - I don't plan on publishing this on PyPi.
- Version
- Use `pytest`.
- Use `black`.
- Don't use `travis`.
- Don't add `pyup` badge?
- Use `Click` for command_line_interface.
- Create author file.
- Use MIT license.

This gives me a good start though I plan on deleting some of the items.

## Automating Initial Setup

The `Makefile` will be able to automate some tasks.
Audrey's `Makefile` is a good start but I plan on using
[flit](https://flit.readthedocs.io/en/latest/) and would like the `Makefile`
also create the initial environment.

### requirements_dev.txt

I removed the exact versions and added the following:

- `flit`
- [`mypy`](https://mypy-lang.org/)
- [`toml`](https://pypi.org/project/toml/)

Once I determine which version I want to keep them to, I will create a pinned
version in my cookiecutter.

### Makefile

In the `Makefile`, I added `lint/typing` and `setup`.
`lint/typing` is to run `mypy`.
`setup` creates a virtual environment, install `requirements_dev.txt` and
run `flit init`.
Later, when I create my `cookiecutter`, I may create `pyproject.toml` with
`cookiecutter` instead.

The main downside to using a Makefile will be how to use it in Windows.
Unfortunately, at work I use Windows 10 to do some of my programming.
I should be able to [GNU Make](https://www.gnu.org/software/make/) but that
will be tested later.

## Cookiecutter

My plan is to [fork](https://github.com/cetyler/cookiecutter-pypackage) Audrey's
template and make modifications.
There will be a separate article at the end to explain the changes I did.
Initially would want to update the `Makefile` and `requirement_dev.txt`.

## Documentation

Documentation will be at minimum in two parts -- for the package/library and
for the developer of that package/library.

### Developer

At minimum there will be a `README.rst` that will describe how to install the
package and some basic information on how to use the package.
It can also be used for user information if they are more technical (ex.
Github).

Mote detailed documentation will use `sphinx` and will also include any APIs.
Developer documentation will not be included with the package through `pip
install`.

I will also use a wiki (Gitea/Github/Gitlab) depending on the project.

### User

At minimum will have `getting_started.rst` if the program is simple enough.
Help should be in the program (beyond how to install the program).
Will use `sphinx` when more lengthy documentation is required.
That documentation will be included in the package and ideally hosted at a
website if publicly shared.

## Git Branches

In the past I have used
[Git Flow](https://github.com/petervanderdoes/gitflow-avh) but there are a
couple of things that I don't care for.
The main problem I have is that when I do a bugfix from my main/master branch,
it will merge to develop but not to main/master.
Since it is only me working on my projects, I will do this manually instead.

### Main/Master Branch

This will be for releases only.
Every commit should be tagged (ex. 4.1.3).
The tagged release will also include the following:

- Overview of what was done in the release.
- A list of features/bugfixes.
  - This should include issue numbers.

I have a git alias `over` which will look at commit comments that contain
`Overview` which I will pipe to `CHANGELOG.rst`.

### Develop

This will be essentially what the next release will be.
Unless it is a minor code addition/change, I plan to create a topical branch for
each new feature or major code change.

### Bugfix

Will typically be a new branch from main/master.
Each bug will have its own branch.
Once it is merged by to main/master, develop will merge from master to get the
fixes.
The name of the branch should be the issue number and a short name of the bug.

### Topical

This will mainly be new features starting from develop.
The branch should be concise and limited to a new feature for example.
That way it makes it easier to revert if there a problem or I decide not to use
the feature.
The name of the branch should be the issue number and a short name of the
feature.

If the branch is for example a more drastic change, it will instead have the
name `major` with a short name of what the change will be.
For example changing the program from a locally run program using SQLite and a
CLI interface to a web service would be major.
Furthermore, while that major code change, you would like the option to
continue to update the CLI, it would make sense to create another branch.

## Semantic Versioning

I plan on using [semantic versioning](https://semver.org/) using
MAJOR.MINOR.PATCH.
This will make it easier to keep track of breaking changes, backwards
compatible features and backwards compatible bug fixes.

## Next Steps

Using Audrey's `cookiecutter` template and making some minor changes, I have a
good start to the project.

The next article will go through the process of creating User Requirements.
Then based on the User Requirements, create Design Requirements and a simple
Roadmap.
