+++
title = 'SQL Window Functions Explained'
date = 2023-06-10T14:30:00-05:00
tags = ['review', 'Anton Zhiyanov', 'sql']
author = 'Christopher Tyler'
summary = "Book review summary of Anton's SQL Window Functions."
draft = false
+++

## Overview

I recently finished Anton's book
[SQL Window Functions Explained](https://antonz.org/sql-window-functions-book/).
While I seen window functions, I only had a basic knowledge.
I originally bought the e-book at the beginning of the year but it has been
recent completed (the last part of the book he released last month).
My review is based on the e-book though keep in mind there is a physical book
available.

## Structure

Anton structured the book into three parts:

* Windows and functions
* Frames
* Practice

Keep in mind that there are practice questions throughout the book.
The last part is more of an advance section that shows what you can do with
window functions.
The book is meant to go through in a linear fashion as he builds up the query
based on the what the requested information each problem is seeking.
While the e-book is a PDF, I didn't have a problem using either my Kindle, iPad
or my computer as the text is quite large.

## Setup

Anton provides `.sql` files that you can download at his website or you can do
it online at his website (I didn't try this out).
I used PostgreSQL as I use that with a lot of my projects but Anton did test
the code with SQLite and MySQL so it should work with those.
I have a training database and created a `wfe` schema for this book, so I had
to modify the `.sql` files.
I then used [pgcli](https://www.pgcli.com/) though using psql would be nearly
as good.

## Impressions

I usually go through a book and skim to see how useful it could be.
This book specifically I bought to help me with my work.
About a third of the way through, I was learning things that I was immediately
applying to my work projects.
For example, generating row numbers was useful as I need to know the test order
for the units under test (UUT).
Some UUTs if they fail the first time may need to get retested and pass two
times in a row in order to be accepted.
I was able to determine which UUTs were able to pass after retest by using a
reverse order by UUT by tester and confirming that the those tests passed.

Understanding frames really help bring home how I can use window functions and
understanding the behavior.
Further, knowing that I could use groups and range beyond just rows expanded on
what I plan on doing with window functions.

The last part of the book Finance, Clustering and Data Cleaning were useful on
how to go through my complex problems step by step creating the window function
before filtering to ensure that it works or using techniques on cleaning data.
Clustering I plan on trying to use when comparing my indoor conditions to the
weather data I get from [OpenWeatherMap](https://openweathermap.org/).
This part I feel like I am going to go through multiple times before I really
understand the concepts.

I went through pretty much all the exercises and didn't really get tripped up.
The quality of the e-book was great and I think I only saw maybe one or two
errors (both were queries missing `round()` based on the results).

## Conclusion

I think that is book is great after progressing through an introduction to SQL.
I would recommend starting with [Memorable SQL](https://payhip.com/b/oXJs) if
you haven't done any SQL coding before getting this book.
If you know some basic SQL coding, I would still read either
[SQL for Data Scientists](https://sqlfordatascientists.com) or
[Practical SQL](https://www.practicalsql.com) before reading Anton's book.

Anton does an excellent job focusing on window functions and showing you the
various ways window functions can help solve problems.
Other books that try to cover everything can't focus on window functions and
tend to provide a high level on how to use them.
For example, in SQL for Data Scientists, Renee dedicates one chapter to window
functions and acknowledges that she is only covering a small amount.
Other books either don't cover window functions or do only a passing remark.

I would say that
[SQL Window Functions Explained](https://antonz.org/sql-window-functions-book/)
is a great buy and an excellent reference.
His [blog](https://antonz.org/all/) is also very useful especially if you use
SQLite.
