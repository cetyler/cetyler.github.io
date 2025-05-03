+++
title = 'How to Run Python in Production'
date = 2025-05-03T15:43:32-05:00
draft = false
tags = ['python','Ashish Bhatia','uv','ruff','git leaks','nosey parker','license check','docker']
summary = 'An informative article from Ashish.'
comments = true
+++

I thought that
[Ashish's article](https://ashishb.net/programming/python-in-production-2/)
had some interesting insights on running Python in production.
Below are some of my thoughts.
Keep in mind that I don't have massively large Python projects in production.
The tools that I created are internal to my company and only my dashboard runs
all the time.

## Project Quality

I generally agree that [uv](https://docs.astral.sh/uv/) is a good place to start.
I use `uv` for Python version management, project management and one-off scripts.
I mostly use [ruff](https://astral.sh/ruff) for my linting and have been able to
reduce the number of linters.
I also make use of `pyproject.toml` as much as possible to config my linters as
well.

Again since my projects are internal, I haven't really checked for secrets though
I will research [Git Leaks](https://github.com/gitleaks/gitleaks) and
[Nosey Parker](https://github.com/praetorian-inc/noseyparker) a try.

## Project Maintainability

More or less agree and I didn't know about
[License Check](https://github.com/FHPythonUtils/LicenseCheck).
I will definitely need to look at this for my personal projects.
I would also add that it is important to have good documentation.
Documentation is not just a ReadMe, it includes documented objects in the
program and a Wiki if the program is in anyway more substantial than a script.

## Deployment

I don't use [Docker](https://www.docker.com) at work.
Initially it was interference with my VMs, then it was confusion with the
[pricing](https://www.docker.com/pricing/) in the past when used commercially
though it does appear that I could use it now at work.
**Note** at work I am forced to use Windows and most of those problems are not
issues using Linux-based or Mac systems.
Again my projects are not massive and using `uv` and virtual environments are
good enough for me.

## Conclusion

Good article and I did learn a couple of nice things.
As always reading how others do things, take what works for **you**.
Not everyone is working at a relatively small company like myself creating only
internal tools and nor everyone works at a huge company like Google that need
to create internal/external programs at scale.
