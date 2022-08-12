Title: Using SQL for Exploratory Data Analysis (EDA)
Date: 2021-05-22 14:30
Category: Blog
Tags: sql, eda
Author: Christopher
Summary: Some use SQL commands that can help with EDA.
Status: published
comment_id: using-sql-for-eda

While I do use [pandas](https://pandas.pydata.org) to do most of my initial
exploratory data analysis (EDA), I do also use SQL.
I started using pandas for EDA at work and quickly started to hit the memory
limits.
I then for various ways to more efficiently use my memory
(chunking, data types, etc.) but was still having issues.
Finally I started using SQL which made it much easier to do analysis on
larger datasets.

This article will focus on some useful SQL commands that can help with initial
EDA.
**Note** I highly recommend reading Memorable SQL.
I will be using PostgreSQL in my examples.
I also was able to get some additional ideas from
[Appsilon](https://appsilon.com/intermediate-sql).

I plan on using my existing data.

## Initial Data View

Initially I look at the first 10 rows or so of a table to get an idea of what I
am working with.

    SELECT * FROM hvac LIMIT 10;

This will get the first 10 rows from `hvac` table.
Now I know the column names, potentially what kind of data that I have.
If I want to look at the last 10 rows for example, I will use the timestamp to
reverse the order.

    SELECT * FROM hvac ORDER BY timestamp DESC LIMIT 10;

Now I have the last 10 rows.

If I have multiple tables, I would do the same thing with each table.
Usually ahead of time I know which tables are related to each other and if I
need to do a join.

Now I may want to know how much data I am dealing with.

    SELECT COUNT(timestamp) FROM hvac;

This will return the number of rows.

    SELECT column_name, data_type
    FROM infromation_schema.columns
    WHERE table_name = 'hvac';

This will return a list of column names and the data type for each column for
`hvac` table.

I could also get the unique values for `location`.

    SELECT DISTINCT(location) FROM hvac;


Within a few minutes, I have an idea of the size of data and what type of
data I have.
If this was done in pandas, I would have had to load all the data first, then
do my EDA.
Actually that is not completely correct as you can read SQL in pandas which
would be similar to what I just did.
My workflow is to do the following:

- If the data is not in a database (ex. csv, xlsx, etc.) put it in a database.

    - SQLite can be really useful especially if you don't need concurrent
      users.

- Do some initial EDA in SQL to determine if it makes sense to do everything in
  pandas or to use a mix of pandas and SQL queries.

- Clean the data.

- Perform some analysis to get some initial insights.

- Share findings and next steps.

## Cleaning Data

Sometimes it makes sense to do certain kinds of cleaning in SQL prior to
loading the data into pandas.
With the `hvac` table there are a couple of things I would want to do

- Convert timestamp from EPOCH to date and time.

- I think name and location may be confusing and want to change the column
  names.

Changing the column names is straightforward if I only care about when I
display the data.

    SELECT timestamp
        ,location AS sensor_location
        ,name AS sensor_position
        ,humidity
    FROM hvac
    LIMIT 10;

I prefer to use snake_case especially if I will load this data into pandas.
If I was going to export the table from PostgreSQL to say a csv file, then
I would change `sensor_location` to `"Sensor Location"` for example.

Changing `timestamp` from epoch, use `TO_TIMESTAMP()`.

    SELECT TO_TIMESTAMP(timestamp) AS "Timestamp"
        ,location AS "Sensor Location"
        ,name AS "Sensor Position"
        ,humidity AS "Humidity"
    FROM hvac
    LIMIT 10;

Let's say I had a problem with the case of `location`, I could use `LOWER()` to
make `location` lowercase of `UPPER()` for uppercase.
I can also use `CONCAT()` if I want to combine `location` and `name`.

    SELECT TO_TIMESTAMP(timestamp) AS timestamp
        ,location AS sensor_location
        ,name AS sensor_name
        ,UPPER(CONCAT(location, ' ', name)) AS sensor
    FROM hvac
    LIMIT 10;

This will combine `location` and `name` with a space between them.

There is more things that I could do but this should give you an idea of what
you can do with this kind of data.

## Using GROUP BY

Aggregating data can be very useful, especially if you have lots of data and
can't fit that data in memory to use pandas.
Let's get the total number of rows if we combine `location` and `name` together.

    SELECT CONCAT(location, ' ', name) AS sensor
        ,COUNT(CONCAT(location, ' ', name)) AS number_of_rows
    FROM hvac
    GROUP BY CONCAT(location, ' ', name);

**Note** that if you include a column in the `SELECT` statement, you must use
it in an aggregation or you must include it in the `GROUP BY`.
With `GROUP BY` you can use `WHERE`.

    SELECT CONCAT(location, ' ', name) AS sensor
        ,COUNT(CONCAT(location, ' ', name)) AS number_of_rows
    FROM hvac
    WHERE temperature < 90
    GROUP BY CONCAT(location, ' ', name);

This will only count if the temperature is less than 90F.
Using `HAVING` will be like `WHERE` but after `GROUP BY` was done.

    SELET name
        ,ROUND(AVG(temperature), 2) AS average_temperature
    FROM hvac
    GROUP BY name
    HAVING AVG(temperature) < 80;

This will get the average temperature by `name` but only include data if the
average temperature is less than 80F.

The syntax is a little different than in pandas but you can do similar things.
If I am doing more complex aggregation and I can fit the data in memory, then
I would use pandas. 

## Math Functions

With this data, let's say that I would want to convert Fahrenheit to Celsius.

    SELECT *
        ,(temperature - 32.0) * (5.0/9.0) AS Celsius
    FROM hvac
    LIMIT 10;

Keep in mind that if you don't want the result to return as an integer, then at
least one value with each math function will need to be a float.
I have found that if I want my result to be a float, I make all my numbers floats.
Also know that if you do keep it as an integer, the result will not round up.

The math functions in general are what you would expect.

- addition `+`

- subtraction `-`

- multiplication `*`

- division `/`

- modulo `%` which will return the remainder of dividing two numbers.

- exponent `^`

- Functions like `COUNT()`, `SUM()`, `AVG()`, `MAX()` and `MIN()`.


This is not an exhaustive list but should give you an idea of what you can do.

## First/Last/Nth Values

You can use `FIRST_VALUE` function to return the value of a specified column
from the first row of the window frame.

    SELECT *
        ,TO_TIMESTAMP(timestamp) AS date_time
        ,temperature - FIRST_VALUE(temperature) OVER (
            PARITION BY temperature
            ORDER BY timestamp
        ) AS diff_temp_from_1st
    FROM hvac
    LIMIT 10;

Above will return all columns and add `date_time` to convert EPOCH to date and
time.
Will also add `diff_temp_from_1st` column that will subract a given row to the
first row's temperature.
It doesn't make much sense with our current data but hope it helps understand
what you can do.

## Getting the Leading or Preceding Value

`LEAD` function will fetch the value of a specific attribute from the next row
and return it in the current row.
It takes two arguments:

- Column name to fetch the next value.

- The number of rows relative to the current row.

As expected, `LAG` function does the opposite.
With our data, I would like know the difference between my HVAC inlet and
outlet temperatures.

    SELECT *
        ,temperature - LAG(temperature, 1) OVER (
            ORDER BY timestamp
        ) AS temp_diff
    FROM hvac
    WHERE location = 'HVAC'
    LIMIT 10;

A bit ugly but it does subtract the current row's temperature with the previous
temperature.

This can be useful to create an elapse time by subtracting the timestamp from
the previous row or create a cumulative of sales.

## Ranking

Lastly, I want to rank the temperature.
The difference between `RANK` and `DENSE_RANK` functions is that `DENSE_RANK`
will return consecutive ranks, while `RANK` will return ranking that if there
are ties, a rank is skipped.

    SELECT temperature
        ,DENSE_RANK () OVER (
            ORDER BY timestamp
        ) AS rank
    FROM hvac
    ORDER BY timestamp
    LIMIT 10;

Then if for example, I wanted the to filter the temperatures by rank, I can.

## Conclusion
Hopefully so far you are starting to get an idea of how useful it can be to
start your analysis with SQL queries first.
Generally speaking all of what I have done above can be done with a small and
large data set.
While you may have to wait longer with a larger data set, it is not done in
memory and will return a result quicker than you would expect.

Make sure comment and save your SQL statements.
TODO put a link to how to structure your statements.
The other reason to save your statement is that you can use those queries in
pandas or recreate it in pandas to match the SQL statement.

I became much more productive using SQL beyond just dumping a table in pandas
and using pandas to do my analysis.