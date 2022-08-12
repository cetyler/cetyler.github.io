Title: Calculator Project -- Tests
Date: 2022-02-06 15:00
Category: Python
Tags: python, project, library, package, pytest, tests
Author: Christopher
Summary: Creating tests for the API.
comment_id: calculator_tests
Status: published
series: Calculator Project
series_index: 4

## Overview

From the 
[previous article]({filename}/python/2022-01-29-calculator_project_requirements.md),
the plan is to create [calculator](https://github.com/cetyler/calculator) in
order to update my Python workflow.
This article will cover creating some initial tests to verify the program will
meet the requirements and what tests would be needed after the initial tests
using 
[Test Driven Development](https://developer.ibm.com/articles/5-steps-of-test-driven-development/).

## Cookiecutter Template

Audrey's template created a test folder structure that for the purposes of this
project can be simplified.
Will delete the `func` and `unit` folders.
For more complicated projects both folders would make sense to organize the
tests.
Also, will be using `pytest`.

## Test to Meet Requirements

Most of the requirements are are related to the API.
The initial tests should be good enough to verify that the program will meet
the requirements.
The goal for now is not to cover all potential edge cases.
So for example, `add()` can take 2 or more numbers.

    > add(1, 2)
    > 3
    > add(1, 2, 3)
    > 6

If `add()` only has 1 number it should be return an error.
Since there are not that many tests, all API tests will be in `test_api.py`.

If this project was a more complicated project, I would keep `func` and `unit`
folders.
Also the initial tests would be functional tests.

### Functional Tests

Functional tests are high level tests that primarily verify that the program
will meet requirements/specifications.
The goal is to ensure that these tests are done early in the process.
For this project I am not going to create any functional tests right now.

A good example would be a program that would take an text file as an input and
would output some simple stats (word count, number of lines, etc.).
A functional test would be verifying that the word count matches what is in the
text file.
Another functional test would be to count the lines and verify that it matches.
Neither functional tests are testing how the program does the counting, just
providing a given input, the program will output the count.

### Unit Tests

Unit tests typically tests a function/class/method.
My goal is typically not trying to get 100% coverage but unit tests are to
ensure that critical functions are tested.
For this project, my plan is to verify each operation works when given a
correct number of numeric values and output the right result.

    def test_add():
        """Verify that add works."""
        basic = Basic()

        assert add(1, 2) == 3

### In Program Tests/Checks

These tests will be in the program/function/class.
For example, won't create a separate `pytest` test to check if a config file
was loaded.
Instead would do a `try` and `except` to verify that I loaded the file and do a
check to ensure that what was loaded has the correct values.
For this project, I probably use this to capture any exceptions like if the
user only provided one number to `add()` as an example.

### Manual Tests

Non automated tests to ensure compliance.
For example in the calculator program, it would be to run the program and try
out some of the operations (add, subtract, etc.), verify that the interface
looks okay, etc.

## Tests due to Bugs

As bugs are found, the goal is to create a test to replicate the bug prior to
fixing it.
For example, if using `add()` only use 1 number but didn't have a check to
verify that more than one number was entered.
The bug would cause the program to crash.
Would add a test to raise an exception.

    def test_add():
        """Verify that add works."""
        basic = Basic()

        ...

        with pytest.raises(NotEnoughNumbers):
            basic.add(1)

After adding the test, verify that it will fail prior to making the change.
Run the test again and it should pass.

## New Feature Tests

Ideally create tests prior to adding new features.
For example, add a feature so that it would be possible to chain together
multiple operations.

    > add(sub(4,3), mul(5,4), 3)
    > 13

Prior to adding the feature, create some tests to first show that this would
fail, then add the new feature.
Furthermore, could use `pytest` feature to skip tests.

    @pytest.mark.skipif(calculator.__version__ < '2.0.0',
                        reason='Breaking change.')
    def test_multiple_operations():
        """Verify that chaining operations works."""
        basic = Basic()

        assert basic.add(basic.sub(4,3), basic.mul(5,4), 3) == 13

        with pytest.raises(NotEnoughNumbers):
            basic.sub(basic.add(5,4,3,2))

## Next Steps

Now that we have some tests created, can now work on implementing the code and
making sure the the API works before creating the CLI GUI interface.
Trying to develop tests prior to working on the code can help ensure that
requirements will be met, help create better code and preparing for new
features ahead of time.

