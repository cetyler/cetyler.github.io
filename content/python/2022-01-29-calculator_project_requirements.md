Title: Calculator Project -- Requirements
Date: 2022-01-29 15:00
Category: Python
Tags: python, project, library, package
Author: Christopher
Summary: Creating the initial documentation of the calculator project.
comment_id: calculator_requirements
Status: published
series: Calculator Project
series_index: 3

## Overview

From the 
[previous article]({filename}/python/2022-01-22-calculator_project_setup.md),
the plan is to create [calculator](https://github.com/cetyler/calculator) in
order to update my Python workflow.
This article will cover creating User Requirements, Design Requirements and a
Roadmap.

## Location of Documents

While we do have Sphinx already set up, in my opinion these documents should be
related to what the calculator package does and how to use it.
User Requirements and Design Requirements will be in Gitea/Github wiki.
Both these documents are more for the developer than the user.
The Roadmap should be in Sphinx as it is useful to the user when features are
planned to be released.

## User Requirements

User Requirements generally are what the developer thinks the user wants based
either by observation, feedback or a spec document.
This document is to translate the available information into something that
could be used to help build a design.

As you see, the
[User Requirements](https://github.com/cetyler/calculator/wiki/User-Requirements)
describes that this will be a simple program that can also be used as a
library.
There are a couple more requirements but for the most part, this describes what
I think the user would want.

The goal is to create the requirements without thinking about how to implement.
For the calculator project, naming Python as the language is a requirement
since this project is to specifically determine a Python workflow.

## Design Requirements

Design Requirements generally are how the developer is planning on how to
implement the program based on the User Requirements.
This document is usually what an 1.0 version of the program.

As you see
[Design Requirements](https://github.com/cetyler/calculator/wiki/Design-Requirements)
shows that there will be two parts -- GUI and API.

### GUI

The GUI will be an interactive terminal interface similar to the Python shell
or like
[pgcli](https://www.pgcli.com/).
Due to how simple this program is, I don't really need to do a long description
on how I plan on implementing the GUI.

### API

The API will be able to call functions to add, subtract, etc.
I did not include a separate section describing `basic.py` but it will support
addition, subtracting, multiplication and division.

## Roadmap

The Roadmap is a proposed feature release plan.
For this calculator, there is not much of a Roadmap.
First need to create `Roadmap.rst` and create a simple release schedule.
Will need to update `index.rst` to include the Roadmap.

As you can see
[Roadmap](https://github.com/cetyler/calculator/blob/develop/ROADMAP.rst) shows
that it is a fairly basic Roadmap.
There is not really a plan for a 2.0.0 release and a 1.0.0 release will cover
everything that was in User Requirements.

Will need to update my fork of Audrey's cookiecutter template to include a
Roadmap file.

## Next Steps

The rest of the documentation is not done but the rest of the documentation can
be completed prior to a release.
Using a combination of the wiki and Sphinx, it keeps a good separation to what
will stay with the repository and what could eventually go to
[Read The Docs](https://readthedocs.org/) or an internal website.

Prior to any writing any code, I will first write tests to ensure that we will
comply with our User Requirements.
The initial tests should cover the API as much as possible.
