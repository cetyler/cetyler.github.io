+++
title = 'Count Number of Lines in a Git Repository'
date = 2024-09-05T00:00:26-05:00
draft = false
author = 'Christopher Tyler'
tags = ['git','xargs','cat','wc','til']
summary = 'If you were ever curious how many lines of code you have in a repo.'
comments = true
+++

Saw this at [StackOverFlow](https://stackoverflow.com/questions/4822471/count-number-of-lines-in-a-git-repository),
I ended up using the following:

```
git ls-files | xargs wc -l
```

This will return the lines for each file, with the total at the end.
Since I was separating between Python and SQL code, I used `*.py` and `*.sql` at
the end respectively.

However, a bit below in the comments, there was a way to get a count in your
working directory:

```
git diff --shortstat `git hash-object -t tree /dev/null`
```

This will return:

```
> git diff --shortstat `git hash-object -t tree /dev/null`
 57 files changed, 2787 insertions(+)
```

While the lines of code does not mean much, it can be helpful to demonstrate
certain things.
For example, I wanted to give a relative number of a project at work on how much
Python and SQL code is required.
There was about twice as much Python as their were SQL code to create the reports.
However, the code to ingest the data from various source, transform and save to
the database, the Python code was less than a quarter to the report program.
