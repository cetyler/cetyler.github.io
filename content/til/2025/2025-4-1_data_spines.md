+++
title = 'Data Spines'
date = 2025-04-01T19:04:02-05:00
draft = false
tags = ['sql','postgresql']
summary = 'A way to fill in data.'
comments = true
+++

It is useful to have data for each day even if the data is not there.
For example:

| sales_date | product | sales |
| ---------- | ------- | ----- |
| 2022-04-14 | A       | 46    |
| 2022-04-14 | B       | 409   |
| 2022-04-15 | A       | 17    |
| 2022-04-15 | B       | 480   |
| 2022-04-18 | A       | 65    |
| 2022-04-19 | A       | 45    |
| 2022-04-19 | B       | 411   |

We need to insert data for 4/16 and 4/17.
Here is the basic concept:

1. Generate or select unique dates.
2. Generate or select unique products.
3. Cross Join (catesian product) all combinations of 1 & 2.
4. Outer Join 3 to your original data.

```sql
WITH global_spine AS (
 SELECT ROW_NUMBER() OVER (ORDER BY NULL) AS interval_id
  ,DATEADD('day'
           ,(interval_id - 1)
           ,'2020-01-01T00:00'::TIMESTAMP_NTZ
          ) AS spine_start
  ,DATEADD('day'
           ,interval_id
           ,'2020-01-01T00:00'::TIMESTAMP_NTZ
          ) AS spine_end
 FROM TABLE(GENERATOR(ROWCOUNT => 1097)
),
groups AS (
 SELECT product
  ,MIN(sales_date) AS local_start
  ,MAX(sales_date) AS local_end
 FROM my_first_table
 GROUP BY product
),
group_spine AS (
 SELECT product
  ,spine_start AS group_start
  ,spine_end AS group_end
 FROM groups AS G
  CROSS JOIN LATERAL (
   SELECT spine_start
    ,spine_end
   FROM global_spine AS s
   WHERE s.spine_start >= g.local_start
  )
)

SELECT g.product AS group_by_product
 ,g.group_start
 ,g.group_end
 ,t.*
FROM group_spine AS g
 LEFT JOIN my_first_table AS t on sales_date >= g.group_start
 AND sales_date < g.group_end
 AND g.product = t.product;
```
