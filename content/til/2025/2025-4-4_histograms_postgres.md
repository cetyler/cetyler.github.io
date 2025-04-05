+++
title = 'Creating Histograms with Postgres'
date = 2025-04-04T19:29:24-05:00
draft = false
tags = ['postgresql','Elizabeth Christensen','histogram','width_bucket','generate_series']
summary = 'A nice article on how to do histograms in PostgreSQL.'
comments = true
+++

[Elizabeth's article](https://www.crunchydata.com/blog/histograms-with-postgres)
does a good job showing how to do histograms.

```sql
SELECT value, width_bucket(value, 0, 100, 10) AS bucket 
  FROM generate_series(0, 100) AS value;
```

## Auto-formatting histogram with SQL

Let’s build out a larger query that creates ranges, range labels, and formats the
histogram.
We will start by using a synthetic table within a CTE called formatted_data.
We are doing it this way so that we can replace that query with new data in the 
future.

```sql
WITH formatted_data AS (
  SELECT * FROM (VALUES (13), (42), (18), (62), (93), (47), (51), (41), (1)) AS t (value)
), bucket_settings AS (
  SELECT
        5 AS bucket_count,
        0::integer AS min_value, -- can be null or an integer
        100::integer AS max_value -- can be null or an integer
), calculated_bucket_settings AS (
	SELECT
	  (SELECT bucket_count FROM bucket_settings) AS bucket_count,
	  COALESCE(
	          (SELECT min_value FROM bucket_settings),
	          (SELECT min(value) FROM formatted_data)
	  ) AS min_value,
	  COALESCE(
	          (SELECT max_value FROM bucket_settings),
	          (SELECT max(value) + 1 FROM formatted_data)
	  ) AS max_value
), histogram AS (
  SELECT
    WIDTH_BUCKET(value, calculated_bucket_settings.min_value, calculated_bucket_settings.max_value + 1, (SELECT bucket_count FROM bucket_settings)) AS bucket,
    COUNT(value) AS frequency
  FROM formatted_data, calculated_bucket_settings
  GROUP BY 1
  ORDER BY 1
 ), all_buckets AS (
  SELECT
    fill_buckets.bucket AS bucket,
    FLOOR(calculated_bucket_settings.min_value + (fill_buckets.bucket - 1) * (calculated_bucket_settings.max_value - calculated_bucket_settings.min_value) / (SELECT bucket_count FROM bucket_settings)) AS min_value,
    FLOOR(calculated_bucket_settings.min_value + fill_buckets.bucket * (calculated_bucket_settings.max_value - calculated_bucket_settings.min_value) / (SELECT bucket_count FROM bucket_settings)) AS max_value
  FROM calculated_bucket_settings,
	  generate_series(1, calculated_bucket_settings.bucket_count) AS fill_buckets (bucket))

 SELECT
   all_buckets.bucket AS bucket,
   CASE
   WHEN all_buckets IS NULL THEN
	   'out of bounds'
	 ELSE
     CONCAT(all_buckets.min_value, ' - ', all_buckets.max_value - 1)
   END AS range,
   SUM(COALESCE(histogram.frequency, 0)) AS frequency
 FROM all_buckets
 FULL OUTER JOIN histogram ON all_buckets.bucket = histogram.bucket
 GROUP BY 1, 2
 ORDER BY bucket;
```

Try modifying the values in the bucket_settings CTE to see how the histogram
responds.
By increasing the bucket_count, min_value, or max_value, you’ll see the
histogram respond appropriately.
If you modify the range to exclude values, using the FULL OUTER JOIN, you’ll see
that all non-classified items are bucketed as “out of bounds”.
