+++
title = 'Use Python for Scripting'
date = 2026-05-02T16:09:57-05:00
draft = false
tags = ['python','bash','powershell','Jean Niklas Lorange']
summary = 'Using Python for scripting especially with uv can replace other scripting languages.'
comments = true
+++

After using [uv](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)
feature to run Python scripts with dependencies for the last few months as well
as reading [Jean's article](https://hypirion.com/musings/use-python-for-scripting)
earlier this year, I have a better idea how I want to write my scripts going
forward.

## Multi OS Support

I am primarily a Linux user and have been since the 90's.
Over the years have done bash scripts mostly calling other Linux commands like
grep, sed, find, etc.
Windows on the other hand, I use PowerShell using the same thought process.
I do use Windows Subsystem for Linux (WSL) but it can be clunky if you are using
WSL to interact with the Windows' side.
Simple scripts I don't think it matters using bash or PowerShell in their native
operating systems.
It starts to fall apart when you want helper scripts that need to work in Linux
*and* Windows.
If I had a Mac as well, I can't depend that grep, sed, etc. will have the same
arguments either.

## Why Python Can Work

Ignoring using `uv`, Python has an extensive standard library where one could
get away with not needing dependencies to do a variety of tasks.
While you can call things like grep, sed, etc. using `subprocess.call()` but
Python's standard library can do a lot what those programs can do.
One thing I learned from Jean's article was the following:

```python
import warnings
warnings.simplefilter("default", DeprecationWarning)
```

Adding that to your Python script will warn you when a particular functions will
be deprecated.
This can be helpful if a script was written with an earlier version of Python
and knowing when a function will need to be updated.

While I have used bash for decades, there are some things I don't use often and
need to look up.
PowerShell I only have a basic understanding and I am **not** motivated to really
learn.
Python is my main programming language and in general easier for me to understand
which makes it helpful when looking at old code.
Another reason Python can be helpful to use is that as you build the script and
it start getting more and more complicated, Python can handle it.
However doing the same thing with bash or PowerShell you can start getting to
the limitations of the language and can start to be hard to understand, at least
for me.

## Some Examples

I first started creating a simple script to verify that my dashboards at work
are down or not and notify me if it is.
I initially was thinking about doing a PowerShell script and using Outlook API's
to send an email.
**Note** Outlook API's only work with Outlook Classic which my company was
migrating away from.
Instead I made use of `uv` feature to add dependencies to a Python script.
At the top of the file, I added the following:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "log-to-db",
#     "requests",
#     "click",
# ]
# ///
```

[log-to-db](https://pypi.org/project/log_to_db/) is a library I created to log
to a database.
My plan was instead of sending an email, log to my PostgreSQL database just like
my other programs and make use of a program that I already created that will
email me an alert when a program logged an error.
Below is a snippet of how I implemented this script:

```python
response = requests.get(url)
if response.status_code == 200:
    db_logger.info(
        message="Website is up.",
        details=dict(
            status=response.status_code,
            url=url,
            version=__version__,
        )
    )
    print(f"The website {url} is up.")
else:
    db_logger.error(
        message="Website is down.",
        details=dict(
            status=response.status_code,
            url=url,
            error_code=3,
            error_code_msg=str(ERROR_CODES.get(3,9)),
            version=__version__,
        )
    )
    print(f"The website {url} is down. Status code: {response.status_code}")
```

There is more to it but this is the basic script which if I get a response of
200, then the website is working, otherwise log that it is down and what the 
status code.
Using `uv` I don't need to create a virtual environment so it makes it easy to
add to Windows' Task Scheduler.
This script I can also use on my Linux systems as well with no changes to the
code.
The total script is just over 100 lines of code.
I used a similar concept for another script so that I replaced a bash script
with a Python script to move specific files around but only if a certain
condition was met.

Another example that does not require `uv` since `helper.py` I keep in the
Git repository for my projects.
Originally for my work projects, I used PowerShell to help me with things like:

- Run tests.
- Build packages.
- Create Changelogs.
- Update SQL Scripts.

The PowerShell script was basically calling other programs to do these operations.
I wanted to convert the script to Python make it more generic so that I could
use the same script for all my projects and be able to pull information from
`pyproject.toml`.
My initial goal is to replace the PowerShell script to Python and then pull data
from `pyproject.toml` the package name and get the package version (or from
`__init__` of the package).
Using `subprocess.call()` made it easy to do my initial goal.
Using `tomllib` I was able to get the data I wanted from `pyproject.toml`.
This was done in under 200 lines of code and the next step will be to generalize
it enough so that I can use the same script for all my projects.

## Conclusion

Using Python can replace bash and PowerShell scripts that start to require more
code.
Python today is easier than it has been in years to install and use.
While for me Python makes this an easy choice, if there is another language that
is cross platform and easy to use for you, I would suggest giving it a go.

