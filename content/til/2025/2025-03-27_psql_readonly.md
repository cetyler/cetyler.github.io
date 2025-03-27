+++
title = "Starting in Read Only Mode the Easy Way"
date = 2025-03-27T12:44:37-05:00
draft = false
tags = ['postgreslq','psql','Kaarel Moppel']
summary = 'Easy way to ensure that you are in read only mode.'
comments = true
+++

From [Kaarel's article](https://kmoppel.github.io/2025-03-27-til-starting-in-read-only-the-easy-way/) where he goes through a couple of different ways to ensure that you are in read only mode.
The main reason is in case you are in Prodcution and don't want to accidently delete something.

```sql
$ PGOPTIONS='-c default_transaction_read_only=on' psql -X
psql (17.4 (Ubuntu 17.4-1.pgdg22.04+2), server 16.8 (Ubuntu 16.8-1.pgdg22.04+1))
Type "help" for help.

postgres=# create table t1();
ERROR:  cannot execute CREATE TABLE in a read-only transaction
```
And why the joy? Although yes, 95% of time I rely on good ol’ psql (backed up by DBeaver in case some data needs to be fixed as well) the nice thing about this approach is that its client agnostic! As setting startup parameters is actually a driver level feature. So one could as well set it from a JDBC connect string:
```sql
jdbc:postgresql://localhost:5432/mydatabase?user=myuser&password=mypassword&options=-c%20default_transaction_read_only%3Don
```
