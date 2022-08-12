Title: Fixed Broken Search 
Date: 2022-05-21 15:30
Category: Blog
Tags: search, pelican, tipue_search, elegant, website
Author: Christopher
Summary: Misconfiguration caused the search on my website to be broken.
Status: published
comment_id: fixed_search

## Overview

I noticed that the search on my website was broken when trying to search
something.
This article will go through what I did to correct the issue and to expand what
I put in my [closed](https://github.com/cetyler/cetyler.github.io/issues/25)
issue.

## Elegant Theme

The Elegant Theme has the ability to include a search feature but when I
initially set up my website, I forgot to enable it.
Using the [information](https://elegant.oncrashreboot.com/add-search) from
Elegant's website.

A couple of lines to change in `pelicanconfig.py`:

    PLUGINS = ['tipue_search']
    DIRECT_TEMPLATES = ['search']

I did not need to change anything else.
