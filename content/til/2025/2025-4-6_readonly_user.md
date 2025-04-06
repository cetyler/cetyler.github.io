+++
title = 'Create Read Only User in PostgreSQL'
date = 2025-04-06T10:34:11-05:00
draft = false
tags = ['postgresql','pg_read_all_data']
summary = 'Creating a read only user.'
comments = true
+++

I did this for Create Figures.
The goal is that each program will have its own user.

```sql
Time: 4.454s (4 seconds), executed in: 4.001s (4 seconds)
raw_test_data> CREATE USER prog_create_figures WITH PASSWORD 'hs2readonly';
CREATE ROLE
Time: 0.026s
raw_test_data> GRANT pg_read_all_data TO prog_create_figures;
GRANT ROLE
Time: 0.005s
raw_test_data>
```
