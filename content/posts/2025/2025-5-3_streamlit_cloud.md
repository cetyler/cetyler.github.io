+++
title = 'StreamLit Cloud'
date = 2025-05-03T13:31:51-05:00
draft = false
tags = ['streamlit','pybites','Zach Merill','open-mateo','openweathermap','openlibrary','github']
summary = 'Use StreamLit Cloud to further understand StreamLit and share.'
comments = true
+++

## Overview

[StreamLit Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud)
is free for public apps only.
I learned about it from reading
[Zach's article](https://pybit.es/articles/from-backend-to-frontend-connecting-fastapi-and-streamlit/)
at pybites.
I have used StreamLit for work but my design of my dashboard is in such a way
that is not very easy to test.
My goal would be to use StreamLit cloud as a learning tool with other
technologies.

## Requirements

While I could directly use an API such as from
[Open-Mateo](https://open-meteo.com) since this will be a public app, I don't
want to inadvertently hammer their free API.
Instead, the requirement will be to make use of a file based database, probably
[DuckDB](https://duckdb.org) so that I can put that in my GitHub repository.
Initially this data doesn't not need to be up to date.
Another requirement would be to have a least one page that will utilize charts
and widgets. I have not used either of these elements before.
Final requirement is to have test coverage for critical areas of the program.

Optional requirement would be to see if there is a way to provide logging and
some basic stats.
Another optional requirement would to have an admin user so that I can log in
and get additional information that I don't want to necessarily display.

## Data Options

Currently I have multiple years of weather data from
[OpenWeatherMap](https://openweathermap.org).
I have access to data from 10 cities and could put some of this data into a
DuckDB file for further analysis.
I also have temperate, humidity and pressure data at various rooms in my house
that I can use as well.
I have some F1 data that is current to 2018.

I can also use the opportunity to get some data from Open-Mateo.
Open-Mateo provides more information than OpenWeatherMap.
I could do a page comparing the differences.
Finally I could also use [OpenLibrary](https://openlibrary.org/developers/api).
Probably would also download some of the data.

## DuckDB

This will be a good opportunity to try out
[Python Function API](https://duckdb.org/docs/stable/clients/python/function).
The data in DuckDB will be in the final format to basically keep the file as
compact as possible.

## StreamLit

The initial page will make use of some simple
[charts](https://docs.streamlit.io/develop/api-reference/charts) as I want to
limit the number of additional packages.
Any [widgets](https://docs.streamlit.io/develop/api-reference/widgets) will be
dependent on the data chosen.

After setting up StreamLit Cloud free tier you have the following:

- Resources per app: 2.7GB
- Private apps: 1
- Public apps: Unlimited

I linked my account with my GitHub but have created any app yet.
These limits should be fine for my initial app.

## Next Steps

I will need to create a GitHub repository and start fleshing out my requirements
and initial design.
I will then work out my Roadmap and build out the tasklist for the initial
release.
The goal of the initial release is not to complete all requirements but to have
a minimum app that I can understand the differences between StreamLit Cloud to
a local instance.
