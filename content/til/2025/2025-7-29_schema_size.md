+++
title = 'Get Schema Sizes'
date = 2025-07-29T20:21:47-05:00
draft = false
tags = ['GitHub CoPilot','postgresql','postgres']
summary = 'Get the size of each schema in a database.'
comments = true
+++

I got this from asking GitHub CoPilot.
I did need to refine it further.

## CoPilot Chat

I used the following prompt:
    Get the total amount of space in postgresql for a given schema.

and the response was:

To get the **total amount of space used by a specific schema** in PostgreSQL,
you can use the following SQL query.
This query sums the sizes of all tables (including indexes and TOAST data)
within the specified schema:

```Sql
SELECT
    nspname AS schema_name,
    pg_size_pretty(SUM(pg_total_relation_size(pg_class.oid))) AS total_size
FROM
    pg_class
JOIN
    pg_namespace ON relnamespace = pg_namespace.oid
WHERE
    nspname = 'your_schema_name'  -- Replace with your schema name
    AND relkind = 'r'             -- Only regular tables
GROUP BY
    nspname;
```

### Explanation:

- `pg_class`: Contains information about tables and indexes.
- `pg_namespace`: Contains schema names.
- `pg_total_relation_size()`: Returns the total size of a table including all indexes and TOAST data.
- `pg_size_pretty()`: Converts the size into a human-readable format (e.g., MB, GB).

Would you like a version of this query that includes size breakdowns by table as well?

I then asked:
    Can you convert the total size to a number?

Yes, you can convert the total size to a numeric value (in bytes) by removing the
`pg_size_pretty()` function from the query. Here's the modified version:

```Sql
SELECT
    nspname AS schema_name,
    SUM(pg_total_relation_size(pg_class.oid)) AS total_size_bytes
FROM
    pg_class
JOIN
    pg_namespace ON relnamespace = pg_namespace.oid
WHERE
    nspname = 'your_schema_name'  -- Replace with your schema name
    AND relkind = 'r'
GROUP BY
    nspname;
```

This will return the total size in **bytes** as a numeric value, which you can
then convert to kilobytes, megabytes, or gigabytes as needed.

## My Changes

As usual when using LLMs or even StackOverflow, it got me close.
I am sure that I could keep asking CoPilot but I wanted to get the columns, not
so much have it write all the code.

```sql
  select nspname as schema_name
        ,pg_size_pretty(SUM(pg_total_relation_size(pg_class.oid))) as total_size
        ,SUM(pg_total_relation_size(pg_class.oid)) as size
   from pg_class
    join pg_namespace on relnamespace = pg_namespace.oid
   where relkind = 'r'             -- Only regular tables
group by nspname
order by size desc;
```

Basically I wanted the total size but I wanted to sort by size in descending
order.
This got me the following result:

```sql
    schema_name     | total_size |    size     
--------------------+------------+-------------
 weather            | 13 GB      | 14368333824
 sensor_data        | 101 MB     |   105422848
 pg_catalog         | 8800 kB    |     9011200
 information_schema | 248 kB     |      253952
 food               | 248 kB     |      253952
 happier            | 80 kB      |       81920
(6 rows)
```

I could do further refinement but this is good enough.

