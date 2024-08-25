+++
title = "Weather Project - Initial Release"
date = 2023-04-30T20:10:00-05:00
tags = ['python', 'project']
author = "Christopher Tyler"
summary = "Initial working release."
series = ["Weather Project"]
draft = false
+++

## Series

{{< series "Weather Project" >}}

## Overview

From the [previous article]({{< ref "/posts/2022/2022-09-02-weather_project_requirements.md" >}}),
the Weather Project is now on
[PyPi](https://pypi.org/project/openweather-report/) and is on
[Github](https://github.com/cetyler/openweather_report).
This article will be a bit of an update and the steps to the initial working
release.

## Current Status

The last update has been quite awhile ago.
The initial goal the project more or less hasn't change but I have change
some of the goals of the project.
This program will still have the goal of pulling data from OpenWeather but for
now only the [One Call API](https://openweathermap.org/api/one-call-3) since
this is a free API and contains a lot of data:

* Current weather
* Minute forecast for 1 hour
* Hourly forecast for 48 hours
* Daily forecast for 8 days
* National weather alerts
* Historical weather data for 40+ years back (since January 1, 1979)

The latest release (0.1.5), `openweather_report` will only get all the data
listed but the last bullet point.

## Switch from Poetry to Flit

In the past year I used [Poetry](https://python-poetry.org/) in multiple
projects at work and the workflow was getting in my way.
Most of my projects are relatively simple and a lot of the features that could
help a large project was slowing me down.
I went back to using [Flit](https://flit.pypa.io/) with
[pip-tools](https://pip-tools.readthedocs.io/en/latest/index.html) and
[pip-chill](http://pip-chill.readthedocs.io/en/latest/readme.html).
This provides what I need while still being performant.

This release I didn't use `pip-tools` and `pip-chill` but will going forward.

## Getting 0.1.5 Released

I already have a crude private version of this program that was getting data
from OpenWeather but it wasn't generic enough to share.

### pyproject.toml

Switching from Poetry to Flit was straightforward.
Instead of using [SQLAlchemy](https://www.sqlalchemy.org/), I decided to use
[aiosql](https://nackjicholson.github.io/aiosql/).
The main reason is that the SQL required to save data is simple and I don't
want it mixed within my Python code like my internal program had.
SQLAlchemy would be overkill.
I also included the development dependencies but only used
[mypy](https://www.mypy-lang.org/) on this release.
Once I get the rest of the tools setup, I will go into more detail of the
settings in my `pyproject.toml`.

I did figure out how to get [pipx](https://pypa.github.io/pipx/) to recognize
that this was a CLI program and not a library by adding the following:

```toml
[project.scripts]
openweather_report = "openweather_report.cli:main"
```

### README.md

I wanted to make sure that the `README.md` had a quickstart as well as
describing what is required to be able to save to PostgreSQL and SQLite.
The [wiki](https://github.com/cetyler/openweather_report/wiki) will still house
the detail documentation.

### CLI Arguments

The program will work using the latitude and longitude of the city you would
like the weather conditions.
The API Key is a required as well.
An invalid API Key will cause OpenWeather to return JSON that describes the
error.
Optionally:

* `--save`: Will either save to JSON file, PostgreSQL or SQLite.
* `--save_path`: This is only for saving to JSON and will default to a
  timestamp filename.
* `--db_string`: This is only for the databases.
  * For PostgreSQL it will be
    `postgres://username:password@host:port/database`.
  * For SQLite it will be the filename.

The program will crash if the save location is incorrect or if a database the
tables not set up ahead of time.

### Save to JSON

This was straightforward since I would just dump to a file.
There is an option to provide a filename but will default to a timestamp
filename.

### PostgreSQL

It requires a schema of `weather` and a table `weather.raw_json_data` which is
described in the README.
Will print to screen if there is an error but won't stop the program from
running.

### SQLite

It is similar to PostgreSQL except there isn't a schema.
The class is similar to PostgreSQL and will get cleaned up in the next release.

### SQL Code

By using `aiosql`, I have the SQL separate from the Python code.
Right now there are two function `save_json_data` and
`save_json_data_no_schema`.
I may decide to separate `openweather.sql` into one from PostgreSQL and one
from SQLite as the project grows.

## Next Steps

I verified that the program works and was able to replace my crusty internal
version.
I did create a helper program so that I could use this program to loop through
the cities I track the weather.
I should provide at least an example of this file so others could do the same.
I need to flesh out the Roadmap and get the program tested before it gets any
larger.

I also would like to explain how to take this data and do some basic analysis.
For example it can be slow to query JSON in PostgreSQL and I plan on showing
how to take the JSON data and put it into separate indexed tables to make
querying more performant.

Finally I really need to revisit [Cookiecutter](https://www.cookiecutter.io/)
to help me be more consistent with my projects.
