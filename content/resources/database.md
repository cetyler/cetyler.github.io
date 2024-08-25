+++
title = 'Database'
date = 2021-04-10T00:00:00-05:00
author = 'Christopher Tyler'
summary = 'Resources on databases.'
draft = true
+++

Any resources below that I have done a more thorough review, I will link to the
posts.

## [The Art of PostgreSQL](https://theartofpostgresql.com/)

This book as of June 2023 I have not completed.
Also I am currently reading the 2nd edition and Dimitri is working on a 3rd
edition that will be based on the PostgreSQL 15.
This book is written for someone who may know other programming languages but
not SQL and specifically no PostgreSQL.
He goes through in great detail how to utilize the features that PostgreSQL has
to offer and show how efficient SQL code can be compared to other languages
like Python or Java.

## [Beginning Database Design](https://link.springer.com/book/10.1007/978-1-4302-4210-9)

Clare's book was using for me to understand how to design my database.
While she doesn't focus on which database to use, it is very helpful on how to
design a database based on the requirements and not as an afterthought.

## [Memorable SQL](https://payhip.com/b/oXJs)

Jeff's book does a good job providing a good intro to SQL.
He uses [PostgreSQL](https://www.postgresql.org/) which prior to reading his
book, I thought it was too much effort to use a proper database.
While [SQLite](https://sqlite.org/index.html) has it uses, using PostgreSQL
enabled me to have my data at work on the server and I can access it from 
multiple PCs.

Jeff provides enough detail to do meaningful queries and shows how to create
and structure a database. 

## [Practical SQL](https://www.practicalsql.com/)

Anthony does an excellent job in looking at how to see data as a means to
building a story with it.
While Anthony does look at data as a journalist, it is very helpful to use some
of the techniques that he explains.
For example, since he typically is getting public dataset, the data tends to be
dirty.
"Interviewing the data" can be a useful while of thinking about the data and
asking questions to better understand what you have and what you may need to do
before you can start to answer your questions.

## [SQL for Data Scientists](https://sqlfordatascientists.com/)

While Jeff goes through and does an introduction to SQL using PostgreSQL, Renee
uses SQL to solve business problems that a Data Scientist could see.
While she uses MySQL, she explains the differences between the popular
relational databases.
While going through the syntax was helpful (as well as learning WITH Statements
and Views), Renee did an excellent job turning a business question into a
technical implementation.
While my title does not say Data Scientist/Analyst, working at Dynamic I do a
lot of data analysis and her book went a long way in helping me do my job.

## [SQL Window Functions Explained](https://antonz.org/sql-window-functions-book/)

Anton does an excellent job going over window functions in SQL.
I knew very little about window functions and after reading a little bit of his
book, I was able to start applying what I learn to queries I used at work.
I used PostgreSQL but he wrote it to support multiple DBMSs.
You can read my [review]({filename}/sql/20230610-window_functions.md).
