+++
title = 'How to Generate a list of Tables to Drop'
date = 2025-03-29T21:08:33-05:00
draft = false
tags = ['sql', 'pg_tables', 'drop_table','postgresql']
summary = 'An easy method to get a list of tables to remove.'
comments = true
+++

To drop tables, you can generate a list of tables from `pg_tables`.
For example, if I generate tables from `generate reports` and I want to
delete by the end date on the table name, I can do the following:

```sql
SELECT 'DROP TABLE IF EXISTS "' || schemaname || '"."' || tablename || '" CASCADE;'
FROM pg_tables
WHERE schemaname = 'generate_reports'
AND (CASE WHEN RIGHT(tablename,8) !~ '^(\+|-)?[[:digit:]]+$'
   THEN NULL::DATE
   ELSE RIGHT(tablename,8)::DATE
   END) < '2022-06-14';
```

This will take for an example
`generate_reports.8l90_stats_dailsummary_20220601_20220608` would get deleted
but if `20220608` was instead of `20220620` then it would
not get deleted.

```sql
DROP TABLE IF EXISTS "generate_reports"."8l90_statstsallallunitdata_20220606_20220613" CASCADE;
DROP TABLE IF EXISTS "generate_reports"."8l90_statstsallsummary_20220606_20220613" CASCADE;
DROP TABLE IF EXISTS "generate_reports"."8l90_statstsalldailysummary_20220606_20220613" CASCADE;
DROP TABLE IF EXISTS "generate_reports"."8l90_statstsallmodelstested_20220606_20220613" CASCADE;
DROP TABLE IF EXISTS "generate_reports"."8l90_statstsallmodelsstats_20220606_20220613" CASCADE;
DROP TABLE IF EXISTS "generate_reports"."8l90_statstsallopfail_20220606_20220613" CASCADE;
DROP TABLE IF EXISTS "generate_reports"."8l90_statstsalltpfail_20220606_20220613" CASCADE;
```

Then I can copy and paste to delete these tables.
