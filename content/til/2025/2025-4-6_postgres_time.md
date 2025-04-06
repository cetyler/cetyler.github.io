+++
title = 'Working with Time in Postgres'
date = 2025-04-06T11:33:38-05:00
draft = false
tags = ['Elizabeth Christensen','postgresql', 'overlaps', 'brin_index', 'tstzmultirange', 'b-tree']
summary = 'Yet another good article from Elizabeth.'
comments = true
+++

From https://www.crunchydata.com/blog/working-with-time-in-postgres

## Overlapping / Intersecting Time

What if I wanted to find all of the trains that were running at a specific time
or now.
You can use the OVERLAP operator with the INTERVAL.

```sql
select count(*)
from train_schedule
where (actual_departure, actual_arrival)
 overlaps (now(), now() - interval '2 hours');
```

## Time Range Types

Postgres also support working with time ranges that include both a single range
and even multiple ranges.
Single ranges of the timestamptz is called tstzrange and one for multiple
ranges would be tstzmultirange.

For example, if we wanted to create a table in our train database that has some
peak travel fares, we could do:

```sql
create table fares (
     peak_id int
    ,peak_name text
    ,peak_times tstzmultirange
    ,far_change numeric
);

insert into fares(peak_id, peak_name, peak_times, fare_change) values
 (1, 'holiday', '{[2023-12-24 00:00:, 2023-12-27 00:00],[2023-12-31 00:00,
  2024-01-02 00:00]}', 50)
,(2, 'peak_summer', '{[2023-05-27 00:00:, 2023-05-30 00:00],[2023-07-03 00:00,
  2023-08-30 00:00]}', 30);
```

And now to query something with the mult-timezone range, Postgres has a special
operator for this, `@>`.
Let's see if travel today is during peak time.

```sql
select * from fares where peak_times @> now();
```

## Indexing Time Columns

Timestamps column indexes work well with the traditional B-tree index as well
as BRIN.
In general if you have tons of data entered sequentially a BRIN index is
probably recommended.

```sql
create index brin_sequential on train_schedule using brin (acutal_departure);
```
