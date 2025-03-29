+++
title = 'Create Table with Existing Table with No Data'
date = 2025-03-28T21:12:09-05:00
draft = true
tags = ['Haki Benita','postgresql','sql']
summary = 'Another Haki tip.'
comments = true
+++

From [Haki](https://hakibenita.com/sql-for-data-analysis).

To create a table similar to an existing table in PostgreSQL, you can use the 
following commands:

```
CREATE TABLE transaction_training AS TABLE transaction WITH NO DATA;
CREATE TABLE transaction_test AS TABLE transaction WITH NO DATA;
```

This is a really handy syntax! We simply tell PostgreSQL to create a table 
similar to another table, but with no data.
