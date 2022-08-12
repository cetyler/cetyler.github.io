Title: Calculator Project -- API
Date: 2022-04-01 21:00
Category: Python
Tags: python, project, library, package, api
Author: Christopher
Summary: Implement API.
comment_id: calculator_api
Status: published
series: Calculator Project
series_index: 5

## Overview

From the 
[previous article]({filename}/python/2022-02-06-calculator_project_tests.md),
the plan is to create [calculator](https://github.com/cetyler/calculator) in
order to update my Python workflow.
This article will cover implementing the API and verifying that the tests pass
before the command line interface (CLI) gets developed.

## Cookiecutter Template

Audrey's template created a MakeFile to aid to performing certain operations.
I will make use of `make test`, `make lint` and `make coverage`.
In order to get `make coverage` to work, I added `pytest-cov`.

## Implement API

Now that I have tests, I can implement the API and verify that my API will meet
the requirements.
If certain functions won't be implemented in a release, I can always skip a test
until that function/feature gets implemented.
For more complicated projects, feature release based on the roadmap can have the
tests developed and use skip until a certain version.

More complicated programs may have multiple files for the API depending on
functionality.
For example, the calculator program now has its API in `calculation.py`.
Let's say in a future release, I add functionality to do complex calculations
like loan terms, calculus or conversions.
Each one of those could have its own file/module.

### Planning the API

When planning the API the User and Design Requirements can dictate how to
create the API.
However most programs can change over time beyond the initial requirements.
Depending the complexity, more design work would be needed as well as some
thought on being able to extend the API without potentially breaking the API.

For example, the calculator program's initial API are in the `Basic()` class.
Each operation is a method in `Basic()` which makes it easy to extend
`Basic()`.
However each method's inputs should be thought through so that the inputs don't
need to change.
For example, the User Requirements did not state how many numbers can be added
together.
To meet the requirements, I could just have `add()` take just two arguments
which is the minimum to add.
However in the future if I needed to extend `add()` to accept more than two
arguments, I may need to break the API which could break programs that use that
API.

### Breaking the API

Breaking the API should only be done if it is really necessary.
As with the example above, breaking an API can affect users of that API.

Breaking the API should cause a major version change.
If possible, notifying the user ahead of time would help them update their
programs to adjust to the changes.
If an API will get removed, then a deprecation warning should be used prior to
removing that portion of the API.
Changing the API should be documented.
Adding to an API especially if it is not a breaking change does not require a
major version change unless it is a large addition.

For example, `Basic()` stores the previous result but it is not automatic.
In order to store the previous result you would need to do the following:

    > b = Basic()
    > b.previous_result = b.add(1, 2)
    > b.previous_result
      3
    > b.sub(b.previous_result, 2)
      1

This at first may not meet the User Requirements.
The User Requirements the previous result is being tracked by the program.
However this is the API and not the program.
As long as the calculator program keeps track of the previous result, we should
be okay.
Let's say that after creating the API this way and working on the CLI, we
decide that it would be easier to have `Basic()` keep track of the result and
to be able to clear the previous result.

    > b = Basic()
    > b.add(1, 2)
      3
    > b.previous_result
      3
    > b.clear_result
    > b.previous_result
      0

This would require an API additional of `clear_result()` and after each
calculation to store in `previous_result()`.

## Next Steps

Now that we have an API that works we can now create the CLI GUI interface.
Most of the work for the program is in the API so the CLI can be fairly simple.

