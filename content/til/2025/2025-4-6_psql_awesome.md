+++
title = 'psql is Awesome'
date = 2025-04-06T11:25:07-05:00
draft = false
tags = ['echo_hidden', 'comp_keyword_case', 'show_all_results', 'pset', 'gdesc', 'gexec', 'postgresql', 'Laetitia Avrot', 'psql', 'service file', 'row_count']
summary = 'Excellent talk from Laetitia.'
comments = true
+++

See https://mydbanotebook.org/conf_talks.html and search for `psql is Awesome`
for the slides and video.

You can get tips at https://psql-tips.org/

## Service File

This file is a config file to connect to a service.

```sql
cat ~/.pg_service.conf
[mydb]
host=localhost
# Port is same as default but I could use port=5432
user=test
dbname=laetitia
```

Then you can connect to `psql`:

```sql
psql service=mydb
psql (15devel)
Type "htlp" for help.

laetitia=> \conninfo
You are connected to database "laetitia" as user "test" on host "localhost"
(address "::1") at port "5432".
```

## Settings

To get the number of rows for the previous query

```sql
laetitia#= select name from pg_settings limit 10;

          name
--------------------------
allow_in_place_tablespaces
allow_system_tables_mods
application_name
archive_cleanup_command
archive_command
archive_library
archive_mode
archive_timeout
array_nulls
authentication_timeout
(10 rows)

laetitia#= select :ROW_COUNT;
  ?column?
------------
        10
(1 row)
```

To default keywords to lowercase instead of upper case (ex. select instead of
SELECT):

```sql
laetitia#=\set COMP_KEYWORD_CASE lower
```

If you want to see the details:

```sql
laetitia#=\set ECHO_HIDDEN on
laetitia#=\dt
******QUERY********
...shows the query that PostgreSQL used to get back a list of the tables in the
database.
```

If you only want the last query result:

```sql
laetitia#=\set SHOW_ALL_RESULTS
```

## Working everyday with psql

To show the query that has too many columns:

```sql
postgres@raw_test_data=#\x
postgres@raw_test_data=# select * FROM "8l90_ts".vw_high limit 2;
+-[ RECORD 1 ]----+---------------------+
| StartDateTime1  | 2019-01-02 05:36:06 |
| ID              | 1                   |
| TransSN         | LF183625UJL70015    |
| TransModel      | 5UJL                |
| TorqueConvNum   | 8Q0L825410700214    |
| StandID         | 51                  |
| TransStatus     | Passed              |
| ExecutionTime   | 938.2469199         |
| StartEPOCH      | 1546407366.000000   |
| UserName        | Jose Luis           |
| Program         | 8L90                |
| Tested1stShift  | t                   |
| Built1stShift   | <NULL>              |
| BuildDate       | 2018-12-28          |
| BuildTimestamp  | <NULL>              |
| Age             | -5                  |
| SentToRootCause | f                   |
| SentToRack      | f                   |
| Accumulator     | f                   |
| ErrorCode       | 0                   |
| ErrorMessage    | <NULL>              |
| idx             | 1                   |
+-[ RECORD 2 ]----+---------------------+
| StartDateTime1  | 2019-01-02 05:59:21 |
| ID              | 2                   |
| TransSN         | LF183615UJL70013    |
| TransModel      | 5UJL                |
| TorqueConvNum   | 8Q0L825410390214    |
| StandID         | 51                  |
| TransStatus     | Passed              |
| ExecutionTime   | 742.6066612         |
| StartEPOCH      | 1546408761.000000   |
| UserName        | Jose Luis           |
| Program         | 8L90                |
| Tested1stShift  | t                   |
| Built1stShift   | <NULL>              |
| BuildDate       | 2018-12-27          |
| BuildTimestamp  | <NULL>              |
| Age             | -6                  |
| SentToRootCause | f                   |
| SentToRack      | f                   |
| Accumulator     | f                   |
| ErrorCode       | 0                   |
| ErrorMessage    | <NULL>              |
| idx             | 2                   |
+-----------------+---------------------+
```

To repeat the last query:

```sql
laetitia=#\g
```

To output data to csv and read it back:

```sql
raw_test_data=# \pset format csv
Output format is csv.
raw_test_data=# \o query_out.csv
raw_test_data=# select * from "8l90_ts".vw_high where "StartDateTime1" > '2023-04-01' limit 10;
raw_test_data=# \! cat query_out.csv
StartDateTime1,ID,TransSN,TransModel,TorqueConvNum,StandID,TransStatus,ExecutionTime,StartEPOCH,UserName,Program,Tested1stShift,Built1stShift,BuildDate,BuildTimestamp,Age,SentToRootCause,SentToRack,Accumulator,ErrorCode,ErrorMessage,idx
2023-04-01 03:09:40,10735,LF230877TJL70002,7TJL,8QML300545658484,51,Passed,821.7289483,1680318580.000000,Jose Luis Carmona,8L45,t,f,2023-03-28,2023-03-29 18:35:20.67-05,-4,f,t,f,0,,84404
2023-04-01 03:31:13,10736,LF230878THL70011,8THL,8QML300545668484,51,Passed,866.8308236,1680319873.000000,Jose Luis Carmona,8L45,t,f,2023-03-28,2023-03-29 17:23:36.593-05,-4,f,t,f,0,,84405
2023-04-01 03:55:19,10737,LF230906TEL70007,6TEL,8QML303343188484,51,Passed,845.9644845,1680321319.000000,Jose Luis Carmona,8L45,t,f,2023-03-31,2023-03-31 21:27:57.34-05,-1,f,f,f,0,,84406
2023-04-01 04:17:42,10738,LF230907TGL70001,7TGL,8QML300545458484,51,Passed,938.1772788,1680322662.000000,Jose Luis Carmona,8L45,t,f,2023-03-31,2023-03-31 22:57:38.027-05,-1,f,t,f,0,,84407
2023-04-01 04:47:52,10739,LF230726UIL70001,6UIL,8Q0L811203455998,51,Failed,287.9390379,1680324472.000000,Jose Luis Carmona,8L90,t,f,2023-03-13,2023-04-03 18:49:33.003-05,-19,t,f,f,0,,84408
2023-04-01 04:54:29,10740,LF230726UIL70001,6UIL,8Q0L811203455998,51,Failed,198.7150991,1680324869.000000,Jose Luis Carmona,8L90,t,f,2023-03-13,2023-04-03 18:49:33.003-05,-19,t,f,f,0,,84409
2023-04-01 05:32:31,10741,LF230906NLL70001,6NLL,8QML228537648483,51,Passed,939.9121306,1680327151.000000,Jose Luis Carmona,8L45,t,f,2023-03-31,2023-03-31 18:50:05.603-05,-1,f,t,t,0,,84410
2023-04-01 06:14:31,10742,LF230906TDL70003,6TDL,8QML228537638483,51,Passed,912.0541454,1680329671.000000,Jose Luis Carmona,8L45,t,f,2023-03-31,2023-03-31 17:23:20.077-05,-1,f,f,f,0,,84411
2023-04-01 06:36:45,10743,LF230906TDL70002,6TDL,8QML228537698483,51,Failed,298.3721537,1680331005.000000,Jose Luis Carmona,8L45,t,f,2023-03-31,2023-03-31 17:06:37.447-05,-1,t,f,f,0,,84412
2023-04-01 06:43:21,10744,LF230906TDL70002,6TDL,8QML228537698483,51,Passed,886.6135021,1680331401.000000,Jose Luis Carmona,8L45,t,f,2023-03-31,2023-03-31 17:06:37.447-05,-1,t,f,f,0,,84413
raw_test_data=#\o
```

`\o` without any options will stop saving to file.
Keep in mind that `\!` will enable you to run any CLI command.
**Note** that if you are using Windows, you may have problems running commands
since it appears to use `cmd.exe` instead of PowerShell.

You can use `\i` can run a query file (ex. `\i query.sql`).

## Getting Deeper

`\watch 1` will repeat the query every 1 second.
`\gdesc` will look at the last query provide the type for each column.

```sql
raw_test_data=# select * from "8l90_ts".vw_high where "StartDateTime1" > '2023-04-01' limit 10;
raw_test_data=# \gdesc
     Column      |            Type
-----------------+-----------------------------
 StartDateTime1  | timestamp without time zone
 ID              | bigint
 TransSN         | text
 TransModel      | text
 TorqueConvNum   | text
 StandID         | text
 TransStatus     | text
 ExecutionTime   | text
 StartEPOCH      | numeric
 UserName        | text
 Program         | text
 Tested1stShift  | boolean
 Built1stShift   | boolean
 BuildDate       | date
 BuildTimestamp  | timestamp with time zone
 Age             | integer
 SentToRootCause | boolean
 SentToRack      | boolean
 Accumulator     | boolean
 ErrorCode       | numeric
 ErrorMessage    | text
 idx             | bigint
(22 rows)
```

`\gexec` Will play the previous statement (ex. think statements that begin with
`begin;` and may end with `rollback;`).
