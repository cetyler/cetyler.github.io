+++
title = 'List Table Columns in PostgreSQL Database'
date = 2025-03-31T20:50:24-05:00
draft = false
tags = ['sql','postgresql']
summary = 'A way to list table columns.'
comments = true
+++

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
