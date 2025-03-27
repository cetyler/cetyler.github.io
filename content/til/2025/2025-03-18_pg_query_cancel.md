+++
title = "Postgres query cancellation"
date = 2025-03-18T11:15:37-05:00
draft = false
tags = ['postgresql','statement timeout']
summary = 'Couple of different ways to add a timeout to a PostgreSQL query.'
comments = true
+++

I took this from [this article](https://pert5432.com/post/postgres-query-cancellation).
Below are only highlights.

## Basic timeouts

If you want to limit how long any query can run for you can use the `statement_timeout` setting. If a query runs for longer than the value of this setting the query will fail. You can update this setting by running:

```sql
SET statement_timeout = '60s'
```

This setting affects any query ran on the same connection.

If you want to have different timeout values for different queries you need to change the setting before running each query, you then also have to make sure to update the setting before running other queries.

For example:

```sql
-- Set timeout for the next query
SET statemenet_timeout = '5s'; 

-- Run the query
SELECT * FROM users; 

-- Set the timeout back to a value that works for most queries
SET statement_timeout = '60s'; 
```

Or you can run each query in a transaction and make use of `SET LOCAL` to change the setting only for the current transaction:

```sql
BEGIN;
SET LOCAL statement_timeout = '5s';

-- Each of these queries will have a timeout of 5s
SELECT * FROM users;
SELECT * FROM accounts;
COMMIT;

-- statement_timeout goes back to the value it was before the transaction
```

Since Postgres 17 there is a `transaction_timeout` setting available as well, you can use this to set a timeout for an entire transaction and hence use it to set a timeout for a group of queries like so:  

```sql
BEGIN;
SET LOCAL transaction_timeout = '5s'
-- This entire transaction has a timeout of 5s

SELECT * FROM users;
SELECT * FROM accounts;
COMMIT;

-- transaction_timeout goes back to the balue it was before the transaction
```

`statement_timeout` and `transaction_timeout` are best used to set a global limit for a maximum duration of a query or a transaction to stop too long queries from hogging too many resources, holding locks for too long etc...
