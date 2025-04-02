+++
title = 'Create Assert Function in SQL'
date = 2025-04-01T18:15:50-05:00
draft = false
tags = ['sql','assert never','error','Haki Benita']
summary = 'Using an assert to instead of sending NULL.'
comments = true
+++

This is from [this article](https://hakibenita.com/future-proof-sql).
The idea is that instead of returning `NULL` when the expectation is that a
value should be return, generate an error so that we know there is a problem.

## Assert Never in SQL

To trigger an error in PostgreSQL we can write a simple function:

```sql
CREATE OR REPLACE FUNCTION assert_never(v anyelement)
RETURNS anyelement
LANGUAGE plpgsql AS
$$
BEGIN
    RAISE EXECPTION 'Unhandled value "%"', v;
END;
$$;
```

The function accepts an argument of any type, and raises an exception:

```sql
db=# SELECT assert_never(1);
ERROR: Unhandled value "1"
CONTEXT: PL/pgSQL function assert_never(anyelement) line 3 at RAISE
```
Tp trigger an error when the query encounter an unknown value, we can call it
when the expression reaches the `ELSE` part:

```sql
db=# SELECT COUNT(*) AS payments
      ,SUM(
            CASE method
                WHEN 'cash' THEN 100
                WHEN 'credit_card' THEN 30 + amount * 0.02
                ELSE assert_neve(method)::INT
            END
        ) AS commison
     FROM payment;

ERROR: Unhandled value "bank_transfer"
CONTEXT: PL/pgSQL function assert_never(anyelement) line 3 at RAISE
```

The query encountered the unhandled payment method `bank_transfer` and failed.
The error also includes the values we forgot to handle, which makes it
especially useful for debugging.
Now we can decide to either fix our query to include `bank_transfer` or just
exclude it:

```sql
db=# SELECT COUNT(*) AS payments
      ,SUM(
            CASE method
                WHEN 'cash' THEN 100
                WHEN 'credit_card' THEN 30 + amount * 0.02
                ELSE assert_neve(method)::INT
            END
        ) AS commison
     FROM payment
     WHERE method IN ('cash', 'credit_card');

 payments | commission
----------|------------
        3 |      500.0
```
