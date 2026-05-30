+++
title = 'The Git Commands I Run Before Reading Any Code'
date = 2026-05-02T18:10:27-05:00
draft = false
tags = ['Ally Piechowski','git']
summary = 'Five git log commands that diagnose a new codebase before you open a single file.'
comments = true
+++

I saw [Ally's article](https://piechowski.io/post/git-commands-before-reading-code/)
and she highlights 5 commands.

## What Changes the Most
```bash
> git log --format=format: --name-only --since="1 year ago" | sort | uniq -c | sort -nr | head -20
```
I run this from `app/` or `src/`, not the repo root.
Lockfiles, changelogs, and generated code will dominate the list otherwise.
This can help determine how much activity a particular module is getting.

## Who Built This
```bash
> git shortlog -sn --no-merges
```
This is less useful to me since most of my projects I am the only contributor.
However this can be really helpful when I am inspecting a new project/library to
determine if I want to use it or now.

## Where Do Bugs Cluster
```bash
> git log -i -E --grep="fix|bug|broken" --name-only --format='' | sort | uniq -c | sort -nr | head -20
```
This is helpful to determine how often and how the contributors in a project fixes
bugs.
For my projects, this can be useful to see which modules I am getting the bugs.


## Is This Project Accelerating or Dying
```bash
> git log --format='%ad' --date=format:'%Y-%m' | sort | uniq -c
```
This is useful looking at other projects and not my own.
Knowing the amount of commits can be helpful for whether a library is active,
maybe too active/volatile or is dying.

## How Often Is the Team Firefighting
```bash
> git log --oneline --since="1 year ago" | grep -iE 'revert|hotfix|emergency|rollback'
```
Again not so much for my projects but can give an indicator on how well a project
is being ran.
