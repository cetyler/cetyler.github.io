+++
title = 'psql Watch Improvements'
date = 2023-11-10T00:00:45-05:00
draft = false
tags = ['psql','postgresql','Luca Ferrari']
summary = 'A good tip found by Luca.'
comments = true
+++

I saw this tip at [Luca's website](https://fluca1978.github.io/2023/09/22/PostgreSQL16psqlwatch.html)

To use `\watch`:

```sql
testdb=# select * from pg_stat_progess_cluster;
...
testdb=# \watch 5
```

The above example will show me what is going on as CLUSTER or VACUUM with a
refresh ratio of 5 seconds.
One problem of the \watch command is that it loops forever, meaning you need to
manually stop it (e.g., CTRL-c).

With PostgreSQL 16, you can now include a count so it will stop.

```sql
testdb=> \?
General
...
  \watch [[i=]SEC] [c=N] execute query every SEC seconds, up to N times
testdb=> \watch i=2 c=7
...
```

This will watch every 2 seconds and stop after 7 times.
The following is also correct:

* `\watch 2` will go forever every 2 seconds.
* `\watch 2 c=7` will go every 2 seconds and stop after 7 times.
  * `\watch i=2 c=7`
* `\watch 2 7` is not valid.
