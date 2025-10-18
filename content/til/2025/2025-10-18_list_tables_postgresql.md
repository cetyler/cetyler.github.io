+++
title = 'List table columns in PostgreSQL database'
date = 2025-10-18T16:13:43-05:00
draft = false
tags = ['postgresql']
summary = 'An easy way to get all the tables in a given database.'
comments = true
+++

Not sure where I saw this but it is a very useful tip.
To get the columns for each table in a database do the following:
```sql
SELECT table_schema
 ,table_name
 ,ordinal_position AS position
 ,column_name
 ,data_type
 ,CASE WHEN character_maximum_length IS NOT NULL
  THEN character_maximum_length
  ELSE numeric_precision
  END AS max_length
 ,is_nullable
 ,column_default AS default_value
FROM information_schema.columns
WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
ORDER BY table_schema
 ,table_name
 ,ordinal_position;
```
I can further filter by schema or a specific table.
