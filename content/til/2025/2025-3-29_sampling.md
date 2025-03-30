+++
title = 'Sampling'
date = 2025-03-29T20:26:00-05:00
draft = false
tags = ['sql','postgresql','sampling','random','bernoulli','tablesample','Haki Benita']
summary = 'Sampling data with SQL.'
comments = true
+++

Another tidbit from [Haki](https://hakibenita.com/sql-for-data-analysis).

## Sampling

Sampling a random portion of a table is a very common when training a model. 
A simple way to fetch a random portion of a table is combining random with 
LIMIT: 

```sql
db=# WITH sample AS (
SELECT *
FROM users
ORDER BY random() LIMIT 10000
)
SELECT count(*) FROM sample;
count
───────
10000
(1 row)

Time: 205.643 ms
```
    
To sample 10K random rows from the table you first sort in a random order, and 
then take the first 10K rows.

Using random to sample data is great, but for very large datasets it can be 
inefficient. 
PostgreSQL provides other methods of sampling a proportion of a table, which are 
more suited for large tables.

PostgreSQL provides two sampling methods, `SYSTEM` and `BERNOULLI`. 
To sample a table, use the `TABLESAMPLE` keyword in the `FROM` clause, and provide 
the sampling method along with it's arguments. 
For example, sampling 10% of the table using the SYSTEM sampling method:

```sql
db=# WITH sample AS (
SELECT *
FROM users TABLESAMPLE SYSTEM(10)
)
SELECT count(*) FROM sample;

count
───────
95400
(1 row)

Time: 13.690 ms
```

The `SYSTEM` sampling method works by sampling blocks rather than rows, which 
makes it very fast. 
The table we sampled contains 1M rows, and the sample returned slightly less 
than 100K rows. 
For large datasets it's not uncommon to compromise accuracy for performance.

Another sampling method provided by PostgreSQL is `BERNOULLI`:

```sql
db=# WITH sample AS (
SELECT *
FROM users TABLESAMPLE BERNOULLI(10)
)
SELECT count(*) FROM sample;

count
────────
100364
(1 row)

Time: 54.593 ms
```
Unlike the `SYSTEM` sampling method, `BERNOULLI` works at the row level 
which makes it a bit slower, but the results are better distributed.

These are the timings for sampling 10% of table with 1M rows using different 
sampling methods:

```sql
| SAMPLING METHOD | TIMING
| --------------- | ------
| random()        | 205ms
| BERNOULLI       | 54ms
| SYSTEM          | 13ms
```

If you need to sample from a large table consider using `TABLESAMPLE`.
