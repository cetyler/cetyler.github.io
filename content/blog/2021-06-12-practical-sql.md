Title: Practical SQL for Data Analysis 
Date: 2021-06-13 20:30
Category: Blog
Tags: sql, pandas, python, postgresql
Author: Christopher
Summary: Great article from Haki Benita on SQL and Pandas.
Status: published
comment_id: practical-sql-data-analysis

[Haki's article](https://hakibenita.com/sql-for-data-analysis) showcase how it
can be better to use SQL instead of just pandas.
This post will not go through all the great examples but will expand on why you
should go read his article.
While his examples are using PostgreSQL, the benefits are true for other
databases.

## Let the Database do the Work

For example at work I have a VM with PostgreSQL installed.
I use that to help understand how databases work and as an interim while I
understand how to create Python programs to interact with MS SQL Server.
My company have MS SQL Server on a proper commercial grade server hardware.

Loading your data into pandas first for simple exploratory data analysis (EDA)
can usually be faster than doing a series of SQL queries.
Keep in mind I don't mean faster as in CPU cycles but human cycles.
It starts to get problematic when the data starts getting large enough that you
may not have enough memory to load it or manipulate it.

If you can off load some of the work to your database server, then you won't
need to worry as much for how much memory on your computer and it will actually 
be faster.
Also you can still use pandas but do some of the transforming of the data in the
SQL query first before loading into pandas.

For work, I had to look at data from the past year.
This data would require joining two tables, looking for failures for a certain
test and getting some stats (min, max, average, standard deviation, etc.).
Normally I would just use pandas but it would be too large with roughly a few
million rows of data with about 10 columns.
Instead I did everything with a SQL query and the only table I loaded into
pandas was my stats which was about 40 rows and 5 columns of data.
This was pretty quick using my PostgreSQL database on my VM but it was much
faster on using my company's MS SQL Server database on a proper server.
If I didn't use a database, I would have had to use some sort of batching
method.

## When Raw Data is NOT in a Database

While my home projects I tend to put my continuous data into PostgreSQL, at work
I don't have that luxury.
While at work we do have data in MS SQL Server, a lot of the tester data is in
MS Access, yuck!
I also get data in Excel spreadsheets, csv and NI tdms files.
Pandas support all the formats I mentioned above and then some.
Again if you are not talking about a lot of data, just load it directly into
pandas.

However if you have a large csv file or an Excel spreadsheet that have many tabs
of data that are related to each other, put it in a database instead.
I personally have a Python program that will batch through my raw data and put
either in a PostgreSQL or SQLite database.
Now I analyze the data easier.

For example, due to the limitation in MS Access every year we start with an
empty MS Access file and archive the previous' year's data.
Normally I don't need to look at data from more than a few months but we had an
issue that we didn't know how far back it went.
I had to look at the last 5 year's worth of data.
I could have batch in the data using pandas and did my analysis.
There are a couple of problems with that:

1. Loading data directly from MS Access into a pandas DataFrame is slow.
2. I could only load about 3-4 months worth of data at a time due to memory
   constraints.
3. While I could load a subset of data and do some EDA, I didn't know what I was
   looking for and the size of my subset will still be too large to load at
   once.
4. As I was finding out more information, I would get different requests which
   means I would have to do 1. each time someone would make a different request.

I decided early on that I would load all the data into SQLite database with the
tables denoted by year (this was due to the data structure not being the same
over the years).
This decision greatly reduced the wait time to load in the data as I took away
the long MS Access load time.
SQLite is much fast to load data into a pandas DataFrame.
Also I could use my SQL query to reduce the data further and only use pandas for
the more complicated analysis.

That lesson informed me to start loading data into my PostgreSQL database for
the production lines that get requested the most.
Now I can respond to a request quicker because I already have the data ready to
go.

## Interim Data

The nice thing about using a database, it doesn't just need to hold your raw
data.
For work I am in the process how migrating away from reading and saving data to
SQLite.
The problem is that each of my programs would have its own data saved in a
unique SQLite files that was not shared.
So if I was doing a project using Jupyter Notebooks, each project would have
raw, interim and processed data.
Instead putting my data into either PostgreSQL or MS SQL Server, it is in one
centralize location.

For example, I put the most requested production line's MS Access data into
PostgreSQL.
I recently got a request to see if the change we made in a part of the
production process and did it reduce the failure rate of a particular test.
My raw data is already in PostgreSQL.
I needed to transform and process the data.
My SQL query that I loaded into my Jupyter Notebook, I did the following:

1. Rename the columns.
2. Made sure that my alphanumeric serial numbers were all in upper case.
3. Combine the date and time columns into a timestamp column and converted that
   into EPOCH.
4. Only include the tests that were affected.
5. Only include the data between certain dates prior and after the change in the
   process occurred.

I then saved this data on PostgreSQL and named the database the same of my
Jupyter Notebook project so I could refer to the data later.
After I did my EDA, I knew what I wanted to share with the team.
Normally I would just dump the tables into Excel and share that but this had to
be more of a presentation.
I decided to save those tables into my project's database.
Finally I created a Jupyter Notebook that would look nice as a presentation and
merely loaded the tables in, added some explanation and displayed the results.

The added bonus with this process is that data is there for my other projects to
get to easily.
When that data gets stale, I just dump it.
The alternative to not using databases would be to save your processed and
interim data in a csv, HDF5, pickle, etc. which each of them have distinct
disadvantages.

## Conclusion

Originally I thought I was going to show some examples but I decided that one
article won't be enough.
Using pandas can be very useful as long as you understand that you will be
memory constraint and it may not be as fast as SQL queries.
The added benefit on using SQL earlier in your analysis is that if you know that
you will be eventually be dealing with larger datasets, using SQL queries won't
change your method.
Using pandas and knowing that you will have to find different ways to fit your
data in memory means that you will need to optimize as you go.

I tend to use both pandas and SQL so that I leverage what both does best.
I plan to write additional articles highlighting what I learned from Haki's
article but with actual data.
Also it will be less of a you should use SQL or pandas but more of this is how
you can do it in either language with some explanation when it could be better
to use one or another.

Now go read [Haki's article](https://hakibenita.com/sql-for-data-analysis)!
