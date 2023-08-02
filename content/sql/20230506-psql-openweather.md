Title: Using psql to put JSON Data into a Table
Date: 2023-05-06 20:00
Modified: 2023-08-01 22:50
Category: SQL
Tags: sql, openweathermap, json, cross lateral join, jsonb_to_recordset()
Author: Christopher
Summary: Show how you can take JSON data and insert that data into a table.
Status: published
comment_id: psql_openweather_json

## Overview

After creating my program
([openweather_report](https://github.com/cetyler/openweather_report)) that
pulls in data from [OpenWeather](https://openweathermap.org), the data is being
saved into PostgreSQL as JSON but I would like to do some basic analysis.
In order to query JSON data:

```
postgres@raw_data=# select raw_data -> 'minutely' -> 0 from weather.raw_json_data limit 1;
                ?column?                
----------------------------------------
 {"dt": 1678704060, "precipitation": 0}
(1 row)
```

I will go in more detail later in the article but this can be a little clunky
but worse it slow down the query.
This article will show how to query JSON data and how to then insert that data
into a table to help with analysis and query performance.

## Querying JSON

The data is using [One Call API](https://openweathermap.org/api/one-call-3).
An example of the JSON:

```
{
  "lat": 39.31,
  "lon": -74.5,
  "timezone": "America/New_York",
  "timezone_offset": -18000,
  "current": {
    "dt": 1646318698,
    "sunrise": 1646306882,
    "sunset": 1646347929,
    "temp": 282.21,
    "feels_like": 278.41,
   ...
}
```

For example, I can do a query to get the timezone for each location that I have
data for the past month:

```
postgres@raw_data=# select distinct raw_data -> 'timezone' as timezone
  from weather.raw_json_data 
 where entry_date >= '2023-04-01'
   and entry_date <= '2023-04-30';
       timezone        
-----------------------
 "America/Chicago"
 "America/Denver"
 "America/Los_Angeles"
 "America/New_York"
(4 rows)
```

The JSON data is in the `raw_data` column and using `->` I can go through each
key in the JSON.
In this example, I didn't need to do anything with the type since it will get
returned as `text`.
If the data was suppose to be numbers, then I would need to use `numeric` for
example.
As you can see, the method to get data out of a JSON column, it is fairly
straightforward.

## Breaking Out JSON to Table

I have about a year's worth of data for 10 locations that I get data for each
location every 20 minutes:

```
postgres@raw_data=# \dt+ weather.raw_json_data 
                                        List of relations
 Schema  |     Name      | Type  |  Owner   | Persistence | Access method |  Size   | Description 
---------+---------------+-------+----------+-------------+---------------+---------+-------------
 weather | raw_json_data | table | postgres | permanent   | heap          | 1235 MB | 
(1 row)
```

If I put just the current weather data into a table:

```
raw_data=# \dt+ weather.current_conditions 
                                          List of relations
 Schema  |        Name        | Type  |  Owner   | Persistence | Access method | Size  | Description 
---------+--------------------+-------+----------+-------------+---------------+-------+-------------
 weather | current_conditions | table | postgres | permanent   | heap          | 30 MB | 
(1 row)

raw_data=# select count(*) from weather.current_conditions;
 count  
--------
 222522
(1 row)

```

Also by having the data into a table, I can add indexes, set up the data in
such a way to make it easier for analyze (ex. convert all the EPOCH to 
timestamp).

The current data is a flat JSON so it should be easy to build the query.
I also want to make it as a view since I will use this to insert data.

```
/* Create View Current Conditions Weather Data from JSON
Created by Christopher Tyler

This will create a view from the JSON data for current weather conditions.
*/

drop view if exists weather.vw_current;
create view weather.vw_current as (
select l.id 
 ,timezone( 
         'UTC'
        ,to_timestamp( 
                (r.raw_data -> 'current' -> 'dt')::integer 
                + (r.raw_data -> 'timezone_offset')::integer)
  )::timestamptz as measured 
 ,timezone(
         'UTC'
        ,to_timestamp(
                (r.raw_data -> 'current' -> 'sunrise')::integer
                + (r.raw_data -> 'timezone_offset')::integer)
  )::timestamptz as sunrise
 ,timezone(
         'UTC'
        ,to_timestamp(
                (r.raw_data -> 'current' -> 'sunset')::integer
                + (r.raw_data -> 'timezone_offset')::integer)
  )::timestamptz as sunset
 ,(r.raw_data -> 'current' -> 'temp')::numeric as temperature
 ,(r.raw_data -> 'current' -> 'feels_like')::numeric as feels_like
 ,(r.raw_data -> 'current' -> 'pressure')::numeric as pressure
 ,(r.raw_data -> 'current' -> 'humidity')::numeric as humidity
 ,(r.raw_data -> 'current' -> 'dew_point')::numeric as dew_point
 ,(r.raw_data -> 'current' -> 'clouds')::numeric as clouds
 ,(r.raw_data -> 'current' -> 'uvi')::numeric as uv_index
 ,(r.raw_data -> 'current' -> 'visibility')::numeric as visibility
 ,(r.raw_data -> 'current' -> 'wind_speed')::numeric as wind_speed
 ,(r.raw_data -> 'current' -> 'wind_gust')::numeric as wind_gust
 ,(r.raw_data -> 'current' -> 'wind_deg')::numeric as wind_deg
 ,(r.raw_data -> 'current' -> 'rain' -> '1h')::numeric as rain
 ,(r.raw_data -> 'current' -> 'snow' -> '1h')::numeric as snow
 ,(r.raw_data -> 'current' -> 'weather' -> 'id')::int as weather_id
 ,(r.raw_data -> 'current' -> 'weather' -> 'main')::text as weather_main
 ,(r.raw_data -> 'current' -> 'weather' -> 'description')::text as weather_description
 ,r.entry_date as entry
from weather.raw_json_data as r
 left join weather.locations as l on (r.raw_data -> 'lon')::numeric = l.longitude
where r.raw_data -> 'current' is not null
);
```

There is a lot here but it is not difficult to go through.
Now with the view, it is now easy to insert the data into
`weather.current_conditions` table.

```
/* Insert Current Conditions Weather Data from JSON
Created by Christopher Tyler

This script will insert data from weather.raw_json_data and put into
weather.current_conditions.
The script will only add data that is current not in current_conditions.
*/

begin;

insert into weather.current_conditions (city_id, measured, sunrise, sunset, temperature, feels_like,
        pressure, humidity, dew_point, clouds, uv_index, visibility, wind_speed,
        wind_gust, wind_deg, rain, snow, weather_id, weather_main, weather_description,
        entry
)
select *
from weather.vw_current
where entry not in (select entry from weather.current_conditions)
 and id is not null
 and measured is not null
order by entry;

commit;
```

This script will use the view as a means to insert the data into the table.
The where clause is to ensure that I am only adding new data, I don't want any
null for id or measured.

This script can be run:

```
> psql "postgres://<username>:<password>@<hostname>:<port>/<db_name>" -X -f current.sql
```

### Nested JSON Data as a List

There is a 60 minute forecast in the JSON data as `minutely`.

```
{
  ...
  "minutely": [
    {
      "dt": 1646318700,
      "precipitation": 0
    },
    ...
    ]
  ...
}
```

This list/array will repeat for another 59 times.
I could do:

```
raw_data=# select raw_data -> 'minutely' -> 0 -> 'dt' as forecast
 ,raw_data -> 'minutely' -> 0 -> 'precipitation' as precipitation
from weather.raw_json_data 
limit 1;
  forecast  | precipitation 
------------+---------------
 1678704060 | 0
(1 row)
```

Again the query is not complicated but this can be annoying to do 60 times.
Instead:

```
raw_data=# select (raw_data -> 'current' -> 'dt') as measured
 ,rows.dt as forecast
 ,rows.precipitation
from weather.raw_json_data
cross join lateral
jsonb_to_recordset(raw_data -> 'minutely') as rows(dt int, precipitation numeric)
limit 10;
  measured  |  forecast  | precipitation 
------------+------------+---------------
 1678704002 | 1678704060 |             0
 1678704002 | 1678704120 |             0
 1678704002 | 1678704180 |             0
 1678704002 | 1678704240 |             0
 1678704002 | 1678704300 |             0
 1678704002 | 1678704360 |             0
 1678704002 | 1678704420 |             0
 1678704002 | 1678704480 |             0
 1678704002 | 1678704540 |             0
 1678704002 | 1678704600 |             0
(10 rows)
```

I included when the forecast was measured or another way when the forecast was
made.
I used `jsonb_to_recordset()` (see
[PostgreSQL's documentation](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-JSON-PROCESSING-TABLE))
and `cross join lateral` (see
[PostgreSQL's documentation](https://www.postgresql.org/docs/15/queries-table-expressions.html))
to be able to unpack the JSON to each forecast has its own row.
**Note** that I did get a hint from this
[Stack Overflow](https://stackoverflow.com/questions/58124750/how-to-turn-a-json-array-into-rows-in-postgresql).

## Conclusion

Being able to save JSON into PostgreSQL is very useful.
In my example of OpenWeather data, I can bring in the data as JSON and process
the JSON to put into tables later.
I could keep the JSON as a backup but only the last 6 months if I wanted to.
Also while I am only using the
[One Call API](https://openweathermap.org/api/one-call-3), my
`weather.raw_json_data` can support any of OpenWeather's other API calls
without changing the table.

