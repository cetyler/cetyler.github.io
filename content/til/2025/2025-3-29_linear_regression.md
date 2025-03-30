+++
title = 'Linear Regression'
date = 2025-03-29T20:57:27-05:00
draft = false
tags = ['linear regression','python','sql','postgresql','scipy','regr_slope','regr_intercept']
summary = 'How to do linear regression with SQL.'
comments = true
+++

Another tip from [Haki](https://hakibenita.com/sql-for-data-analysis)

Another common tool for analyzing data is linear regression.
For example, performing linear regression using Pandas and Scipy: 

```python
>>> import pandas as pd
>>> import scipy.stats
>>> df = pd.DataFrame([[1.2, 1], [2, 1.8], [3.1, 2.9]])
>>> slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df[0], df[1])
(1.0 -0.2000000000000004 1.0 9.003163161571059e-11 0.0)
```

Most developers probably don't expect the database to have statistical 
functions, but PostgreSQL does: 

```sql
WITH t AS (SELECT * FROM (VALUES
(1.2, 1.0),
(2.0, 1.8),
(3.1, 2.9)
) AS t(x, y))
SELECT
regr_slope(y, x) AS slope,
regr_intercept(y, x) AS intercept,
sqrt(regr_r2(y, x)) AS r
FROM
t;

   slope        │      intercept       │ r
────────────────────┼──────────────────────┼───
1.0000000000000002 │ -0.20000000000000048 │ 1
```
 
Using statistical aggregate functions in PostgreSQL we got results similar to 
scipy.
