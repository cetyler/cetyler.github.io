+++
title = 'Rebuild Pelican Source' 
date = 2024-08-11T15:54:00-05:00
lastmod = 2024-08-26T01:00:00-05:00
draft = false
author = 'Christopher Tyler'
tags = ['pelican','python','hugo','git','git submodules','pyenv','pelican-jupyter']
summary = 'More work than expected to get my development system to work with Pelican.'
comments = true
+++

## Overview

I had a couple of issues with my computer that I was using to work on this
website.
Technically this shouldn't be that big of a deal as my code is on GitHub, so it
should just be creating a virtual environment and running `make html`.
However my documentation wasn't quite up to scratch.

## Git Submodules

I don't use submodules much and had to look up the documentation to get
`pelican-plugins` and `pelican-themes` updated after `git clone`.
I had to do a `git submodule init` and `git submodule update` which mostly
worked.
I then had to do `git clone https://github.com/Pelican-Elegant/elegant` in
`pelican-themes/elegant` as that folder was empty which again wasn't documented.

## Creating Virtual Environment

I use [pyenv](https://github.com/pyenv/pyenv) to create virtual environments and
to download various versions of Python.
My documentation doesn't mention which version of Python to use.
Initially I thought I could just use 3.12 and update the packages.
However, [Pelican Jupyter](https://github.com/danielfrg/pelican-jupyter) has
been archived in 2023.
I had to guess the version by looking at when I created this website (3.9).
After that I was able to get it to work.

## Lack of Documentation

Most of the problems above are related to a lack of documentation.
I did have a simple `README.md` that wasn't updated and didn't include some of
the tooling that I updated to make my life easier to post.
I ended up looking through my commits and reading some of the scripts before I
remembered the process to updating my website.

## Next Steps

While I got the website ready to start adding articles, I not sure that this
setup is sustainable.
The main issues is that I would need to update to the latest Python, with updated
packages.
I would then have to replace Pelican Jupyter since it is no longer being
updated.

I did do some research to switch to [Hugo](https://gohugo.io) since it appears
much more activity (release last week) than Pelican (release last year).
I still haven't decided what I will do and may just stay with Pelican for now.
I need to sit down and determine what I want going forward beyond:

- Optional dark theme.
- Quicker method to write and publish (probably using GitHub Actions).
- Less dependencies.
