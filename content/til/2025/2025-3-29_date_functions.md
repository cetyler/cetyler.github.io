+++
title = 'Date Functions'
date = 2025-03-29T20:46:37-05:00
draft = false
tags = ['postgresql','date_part','to_char']
summary = 'Different ways to extract values of a date.'
comments = true
+++

n PostgreSQL, you can easily extract values from date columns.
You will see the most used date functions below.

```sql
SELECT
date_part('year',hire_date) AS year
,date_part('month',hire_date) AS month
,date_part('day',hire_date) AS day
,date_part('dow',hire_date) AS dayofweek
,to_char(hire_date,'Dy') AS day_name
,to_char(hire_date,'Month') AS month_name
,hire_date
FROM employees

| year | month | day | dayofweek | day_name | month_name | hire_date  |
| ---- | ----- | --- | --------- | -------- | ---------- | ---------- |
| 2006 | 4     | 20  | 4         | Thu      | April      | 2006-04-20 |
| 2009 | 1     | 26  | 1         | Mon      | January    | 2009-01-26 |
| 2010 | 5     | 17  | 1         | Mon      | May        | 2010-05-17 |
```
