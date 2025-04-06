+++
title = 'Improving GROUP BY with CREATE STATISTICS'
date = 2025-04-06T11:03:29-05:00
draft = false
tags = ['postgresql', 'create statistics', 'explain_analyze','group by','Hans-Jürgen Schönig']
summary = 'Improve planning by using Create Statistics from Hans.'
comments = true
+++

From
https://www.cybertec-postgresql.com/en/improving-group-by-with-create-statistics

## Creating Sample Data

Create some sample data:

```sql
> CREATE TABLE t_timeseries (
     t   TIMESTAMPTZ
    ,val NUMERIC DEFAULT random()
    );
CREATE TABLE

> INSERT INTO t_timeseries SELECT *
  FROM GENERATE_SERIES('2022-01-01', '2024-12-31', '1 second'::INTERVAL);
INSERT 0 94608001
```

This will insert 94M rows.
Finally you can create optimizer statistics for this data:

```sql
>  ANALYZE;
ANALYZE
```

## GROUP BY Queries Featuring Expressions

What you want to do now is to count how many entries we can expect per day.
You can use `DATE_TRUNC` function which turns a precise timestamp into day,
week, month, etc.

```sql
> EXPLAIN ANALYZE
  SELECT DATE_TRUNC('day', t), COUNT(*)
  FROM t_timeseries
  GROUP BY 1;
```

The problem is that the planner estimates that the GROUP BY will return 94M
rows.
The planner thinks that it's grouped by second instead of day.

## CREATE STATISTICS: Helping the PostgreSQL Optimizer

The reason for the failure is that PostgreSQL does have statistics for the
column but it does not have statistics about the expression (= the output of
DATE_TRUNC).

CREATE STATISTICS is a good way to tell the system keep track of additional
statistics which can help the planner:

```sql
> \h CREATE STATISTICS
```

This will get you help description of the command.
We can tell PostgreSQL to keep track of multi-column related statistics, but
also about expressions.

```sql
> CREATE STATISTICS mystats
   ON (DATE_TRUNC('day', t)
   FROM t_timeseries;
CREATE STATISTICS

> ANALYZE;
ANALYZE
```

The system is will now sample for `DATE_TRUNC('day', t)` and maintain this
information just like simple column-related statistics.

```sql
> EXPLAIN ANALYZE
  SELECT DATE_TRUNC('day', t), COUNT(*)
  FROM t_timeseries
  GROUP BY 1;
```

Now PostgreSQL has changed to a parallel query will return 1,096 rows instead
which the estimate was 1,095.
