+++
title = 'Interpolation'
date = 2025-03-29T20:52:38-05:00
draft = false
tags = ['pandas','python','sql','Haki Benita','fillna','coalesce']
summary = 'One method to fill in data.'
comments = true
+++

Yet another from [Haki](From https://hakibenita.com/sql-for-data-analysis).

## Back and Forward Fill

Filling values with constants is easy, but not always possible. 
Another common interpolation technique is filling empty values with previous or 
following non-missing values.

Pandas offers several variations on back and forward filling, for example: 

```python
>>> import pandas as pd
>>> import numpy as np
>>> df = pd.DataFrame(['A', 'B', np.NaN, 'D', np.NaN, np.NaN, 'G'])
>>> df.fillna(method='ffill') # or df.ffill()
>>>    0
0  A
1  B
2  B
3  D
4  D
5  D
6  G

>>> df.fillna(method='bfill') # or df.bfill() or df.backfill()
0
0  A
1  B
2  D
3  D
4  G
5  G
6  G
```

To achieve the same using SQL, you can use a subquery: 

```sql
WITH tb AS (
SELECT * FROM (VALUES
    (1, 'A' ),
    (2, 'B' ),
    (3, null),
    (4, 'D' ),
    (5, null),
    (6, null),
    (7, 'G' )
) AS t(n, v)
)
SELECT
*,
-- Find the next not null value
coalesce(v, (
    SELECT v
    FROM tb AS tb_
    WHERE tb_.n < tb.n AND v IS NOT NULL
    ORDER BY n DESC
    LIMIT 1
)) AS ffill_v,

-- Find the previous not null value
coalesce(v, (
    SELECT v
    FROM tb as tb_
    WHERE tb_.n > tb.n AND v IS NOT NULL
    ORDER BY n ASC
    LIMIT 1
)) as bfill_v
FROM
tb;

n │ v │ ffill_v │ bfill_v
───┼───┼─────────┼─────────
1 │ A │ A       │ A
2 │ B │ B       │ B
3 │ ¤ │ B       │ D
4 │ D │ D       │ D
5 │ ¤ │ D       │ G
6 │ ¤ │ D       │ G
7 │ G │ G       │ G
```
 
The SQL version is a bit longer, but it is fairly expressive, and it gives great 
flexibility.

**NOTE:** It's tempting to use the window function LEAD and LAG here, but these 
function can only be used when filling single row gaps. 
Once you have more than one consecutive missing row, LEAD and LAG may leave you 
with missing values.
