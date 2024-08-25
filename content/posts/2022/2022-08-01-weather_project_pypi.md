+++
title = "Weather Project - PyPi"
date = 2022-08-11T20:00:00-05:00
tags = ["python", "project"]
author = "Christopher Tyler"
summary = "Setup PyPi with an empty project to lock in the project name."
series = ["Weather Project"]
draft = false
+++

## Series

{{< series "Weather Project" >}}


## Overview

From the [previous article]({{< ref "/posts/2022/2022-07-19-weather_project.md" >}}),
the Weather Project will be put on PyPi to help me understand that process and
to also share with others.
This article will go over how to put a skeleton project on PyPi.

**Note** prior to the completion of this article, I found 
[Rodrigo's article](https://mathspp.com/blog/how-to-create-a-python-package-in-2022)
though keep in mind that his article is much more comprehensive.

## Create PyPi Account

It is fairly straightforward to create an account.
Go to https://pypi.org/account/register/ and follow the instructions.
I would suggest adding at least two emails to your account in case something
happens to one of your email accounts.
I would also setup Two Factor Authentication (2FA).
In order to push our packages to PyPi, create an API token.
I put it in my password manage since I created one to use for all my packages
in PyPi.

You should do the same steps and create an account on https://test.pypi.org/.

## Create Weather Package on PyPi

This may seem backwards, but it is easier to check if a name exists first as
opposed to coming up with a name, creating a git project, then finding out that
your name you selected is too similar to an existing project.
I did a search to make sure that `openweather-report` was not in use though it
took a couple of tries.
I use [pyenv](https://github.com/pyenv/pyenv) to set my Python version so I
created a folder and set the version to 3.10.6 (current at the time of this
article) as well as create my virtual environment.
I created a project using [Poetry](https://www.python-poetry.org/).
This will be an empty project just to lock in the package name.
Add the API token for both PyPi and Test PyPi using:

```bash
$ poetry new openweather-report
$ poetry config repositories.testpypi https://test.pypi.org/legacy/
$ poetry config pypi-token.pypi [API KEY]
$ poetry config http-basic.testpypi [API KEY]
$ poetry build
$ poetry publish -r testpypi
```

If everything works, then the package name is unique enough and it now locked
in.

> **Update:**
> I switched from using Poetry and use Flit.

### Using Flit

Create a token at [PyPi](https://pypi.org/manage/account/).
Using [PyPa](https://packaging.python.org/en/latest/specifications/pypirc/)
instructions, I updated `.pypirc`:

```toml
[distutils]
index-servers =
        pypi
        testpypi

[pypi]
username = __token__
password = <api-token>
 
[testpypi]
username = __token__
password = <api-token>
```

Now to build and publish using flit:

```bash
$ flit init
$ flit build
$ flit publish --repository testpypi
```

## Create Project on Github

Normally I use a private [Gitea](https://gitea.io/en-us/) instance on my local
network for personal projects and another one while I am work.
Openweather-report I would like to share with others.
While I have a [Gitlab](https://about.gitlab.com/) account, most of the
momentum is on [Github](https://github.com/) so at least initially I was start
there.
Add a new repository called
[openweather_report](https://github.com/cetyler/openweather_report).
My goal is to use this project to try and understand some of the features that
are Github provides.
This project is going to be more than just a toy project but this project won't
be overly complicated.
There is enough to the project that I can learn how to use [Github
Actions](https://github.com/features/actions) for example.

## Git Flow

Prior to pushing my project to Github, I used 
[Git Flow](https://github.com/petervanderdoes/gitflow-avh/) but I plan on using
it differently than I have in the past.
This project will have the following branches:

* main
    * This branch will be considered the stable branch.
* release_xxx
    * This will be the next release.
    * There can be multiple releases open (as pull requests).
* feature
    * Any feature to add to develop branch.
    * This will be a short running branch no more than a couple of days.
* bug
    * This can be off either main.

I also plan on doing pull requests instead of just branching from my local git
repository.
This may remove the need to use Git Flow.

## Next Steps

I now have PyPi set up and my project on PyPi and on Github.
The goal is the next release will be a functional release.
The next article will be to start working on the requirements and create a
Roadmap.
