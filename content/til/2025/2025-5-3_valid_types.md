+++
title = 'Validating Data Types from Semi-Structured Data Loads in Postgres with pg_input_is_valid'
date = 2025-05-03T16:08:59-05:00
draft = false
tags = ['pg_input_is_valid','Elizabeth Christensen','postgresql']
summary = 'Yet another excellent article from Elizabeth.'
comments = true
+++

[Elizabeth's article](https://www.crunchydata.com/blog/validating-data-types-from-semi-structured-data-loads-in-postgres-with-pg_input_is_valid)
explains how PostgreSQL versions, 16, 17 and newer have a new function to help
with data validation:
[pg_input_is_valid](https://www.postgresql.org/docs/17/functions-info.html#FUNCTIONS-INFO-VALIDITY).
She goes through and explain how this can be helpful for validating data for
column changes or loading data.

I can see using this for converting JSON data into a table or loading CSV data
into a temp table like Elizabeth did and then insert the data into a new/existing
table by validating the data as it goes in.

I can see trying this out and probably creating an article though it probably
won't be as good as her.
