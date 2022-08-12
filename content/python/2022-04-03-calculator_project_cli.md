Title: Calculator Project -- CLI
Date: 2022-04-03 16:00
Category: Python
Tags: python, project, library, package, cli
Author: Christopher
Summary: Implement CLI.
comment_id: calculator_cli
Status: published
series: Calculator Project
series_index: 6

## Overview

From the 
[previous article]({filename}/python/2022-04-01-calculator_project_api.md),
the plan is to create [calculator](https://github.com/cetyler/calculator) in
order to update my Python workflow.
This article will cover implementing the CLI.

## Determining the Interface

According to the User Requirements, the CLI will be an interactive environment
with no command line arguments.
The inspiration for the interface I am thinking of comes from
[pgcli](https://github.com/dbcli/pgcli).
I would like at least initially be able to do the following:

- Start the prompt with a statement to run help to get a list of commands.
- Be able to press the up arrow or something to go through the history.

A bonus would be able to provide some syntax highlighting and predictive
showing of a command as the user start to type.

### Interactive CLI

Will use [prompt toolkit](https://python-prompt-toolkit.readthedocs.io/) to
create my CLI interface.
This library will also provide me code completion, history and suggesting stuff
from history.

### Add Some Color

Will use [rich](https://rich.readthedocs.io/en/latest/) to add some color to my
interface.
The color will only be added when items are printed out.

## Setup to Run as a Package

First step is to create `__main__.py` so that when this project is ran as a
package, it will start the CLI.

## Building CLI

Using `rich` and `prompt_toolkit` we have enough to meet the User Requirements.
The first step is to determine how to parse the user input.
Due to the User Requirements, the program will need to determine the following:

    > add(1,2)
       |  | |<-- 2nd number to add.
       |  |<---- 1st number to add.
       |<------- add function.

`process_input()` will separate the numbers from the command.
The previous result, the user can use `ans` in a function or as a command which
would return the previous result.
The numbers will initially be strings so the numbers will need to be converted
to numbers.

Next is to execute based on the command given.
Commands like `ans`, `help` and `quit` don't have any additional values.
Math functions like `add()` will run the function with the numbers given.
After math functions are done, update the previous result `ans`.

## Catching Errors

`Basic()` already has some checks to verify that there are enough numbers or
divide by zero.
However, `Basic()` assumes that the values being given are numbers.
While processing the user input, will verify that numbers are numbers and will
let the user know of the problem.

This program only has a limit number of commands.
Will do a check that if any other non command is used, let the user know of the
error.

## Next Steps

The calculator program now works and currently meet the User Requirements.
The documentation will need to be updated prior to a 1.0 release.
Also prior to a 1.0 release, should create a package and verify that it will
still work.
Then can go through and create a checklist to update Audrey's cookiecutter.
Finally, update my Python workflow.
