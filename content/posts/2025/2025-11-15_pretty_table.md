+++
title = 'How to Select Python Libraries'
date = 2025-11-15T23:21:16-06:00
draft = false
tags = ['python','pretty_html_table','Renaud Viot']
summary = 'Found a library that suits my needs but may also be abandoned.'
comments = true
+++

## Overview

In modern programming it is almost expected that you will need to use code
written by someone else in your own code.
However there are times when you should or shouldn't use that code.
This article will be covering
[pretty_html_table](https://github.com/sbi-rviot/ph_table) and why I decided to
use this library even though it looks to be dead.

## Outlook and Tables

At work many people prefer to receive reports through email.
The reports I generate using Python are not pretty but can vary in size.
Sometime last month, Microsoft did an update to Outlook Classic where emails
with either a number of tables or a few tables on the larger side would
cause Outlook to hang and either crash or freeze for 10 minutes or more.
However in New Outlook, it doesn't crash but if you want to forward those
emails with basic formatted tables, Outlook would automatically change the
format and remove the lines around the rows and columns making it harder to
read.
Not sure why [Microsoft](https://support.microsoft.com/en-us/office/feature-comparison-between-new-outlook-and-classic-outlook-de453583-1e76-48bf-975a-2e9cd2ee16dd)
have so many problems naming their software.
Based on this information, I manually creating tables that were
formatted in Excel and noticed that the format would not change if I forward
the email in New Outlook.

## Formatting Tables in Python

I was using
[to_html() method](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html)
in Pandas and there is a section on how to improve the look of HTML tables
using [CSS](https://pandas.pydata.org/docs/user_guide/style.html#More-About-CSS-and-HTML).
Before I attempt to learn CSS, I thought there should be a library already out
there.
Not sure if it was from one of my weekly Python newsletters or a podcast but I
stumbled upon `pretty_html_table` that Renaud Viot created.
The library's README was easy to understand and more important it very succinctly
described of to solve my problem!

## Reviewing pretty_html_table

The first concern that I had when I went to
[Github repo](https://github.com/sbi-rviot/ph_table) was that `pretty_html_table`
hasn't been updated in more than 3 years.
There were 4 pull requests, one of recent as 2024 and none had any comments
from the owner of this project.
Looking at the open issues, only 1 open issue the project owner answered and that
was from 2022.
While there have been 10 contributors, so far everything about this project tells
me that it is dead.

I decided to try [PyPi Plus](https://pypiplus.com/project/pretty-html-table/)
since this would be a good project to see what information I glean that way.
PyPi Plus gives this project 77 out of 100 health due to not being updated in
4 years and not including a Python version requirement.
There are 18 other Python packages that are dependent on this project.

Finally I took at look at the code and realized it was just one file!
Poking around the code was easy enough to read and the file only have ~240
lines of code.
Renaud basically takes the HTML output from Pandas and manipulates it to do the
different table styles.

## Trying pretty_html_table

I took one of my report programs and gave `pretty_html_table` a try.
It was simple to add and the resulting tables style solved my problem.
I did needed to play with the column widths for certain columns as I didn't like
how automatically setting the width worked.
I also couldn't use `pretty_html_table` on tables where I was using `.apply()`
to call a function to highlight cells that met certain criteria however it was
only one table and that report was only sent to a handful of people.
After not seeing any showstoppers, I added `pretty_html_table` to my high
visibility reports.

## Next Steps

Part of my decision process was that `pretty_html_table` was a simple library.
The short term was to use the library as is.
Long term, I will fork the project so that I add some missing features.
Before I add any features, I want to add some tests (currently there are none)
and switch from `setup.py` to `pyproject` and `uv`.
Some features I would like to add are:

- Expand the conditional formatting beyond changing colors for min/max.
  - For example, I have a table where I highlight common values across multiple
    columns.
- Change `width_dict` from a List to a Dict so that you specify the columns by
  name.

## Conclusion

I hope this example was helpful.
I wanted a simple example to show how being thoughtful on which library you
decide to add to project could look like.
Also be aware that with open source software, the project owner has no obligation
to keep working their project/library/code.
Below are some basic steps to take when evaluating whether or not to use someone's
code.

### Check how often a project has been updated

This doesn't mean that a project that haven't been updated in awhile you should
run away.
Many times, the library is done and nothing really needs to be changed.
However if you see issues and pull requests without any interaction with the
project owner, then it could mean that library could be abandoned.
Usually if a project is large like Pandas, I don't worry about it going away.
If a project only have a handful of contributors, then I assume that the project
could be abandoned.

### Review the Code

If the code base is simple in that if the project owner stopped developing the
project, you could maintain it yourself, then the risk is low.
If the code base is larger or not well written or just simply beyond your
experience, then be wary.
Again large projects like Pandas, I did poke around the code but for curiosity not
to see if I could determine that I could modify it on my own.
Small projects I feel like I need to have some confidence that I could maintain
it if I needed to otherwise I need to be prepared to change projects if that
project was abandoned.
If there are tests, that will greatly increase my confidence in the project.

Also check how many dependencies are used.
Remember that for each dependency, you should check each one.
`pretty_html_table` doesn't show any dependency though it actually does --
Pandas.
Pandas can have between 6 and 43 dependencies depending on the optional
dependencies you need.

### Perform a Risk Assessment

This can include a security risk assessment but for my example this is more of
how much of a risk would adding this library to my project.
`pretty_html_table` was merely to improve the look of my tables in my emails.
The side benefit was that I could migrate to New Outlook.
However if something happened and I couldn't use `pretty_html_table` and I didn't
have time to do a fork, I could revert back to the basic Pandas HTML tables.
Since I did review the code, I knew that if Pandas did a change to their HTML
output that would break `pretty_html_table`, I could make those changes myself.
A more sophisticated library like Pandas, I would need to understand that if it
went away, that I would need to do a major rewrite of my code to use a different
library.
However say if I was using Pandas but very simply (maybe using a handful of
methods).
Then the risk goes down a lot because I could switch to Polars, DuckDB, etc.
as long as those libraries have the methods that I am looking for.

