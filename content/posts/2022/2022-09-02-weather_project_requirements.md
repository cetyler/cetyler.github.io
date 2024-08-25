+++
title = "Weather Project - Requirements and Roadmap"
date = 2022-09-16T20:00:00-05:00
tags = ['python', 'project', 'documentation']
author = "Christopher Tyler"
summary = "Create a roadmap and requirements."
series = ["Weather Project"]
draft = false
+++

## Series

{{< series "Weather Project" >}}

## Overview

From the [previous article]({{< ref "/posts/2022/2022-08-01-weather_project_pypi.md" >}}),
the Weather Project is now on
[PyPi](https://pypi.org/project/openweather-report/) and is on
[Github](https://github.com/cetyler/openweather_report).
This article will start going through the requirements and to develop a
Roadmap.

## Requirements

Initially, all documentation will reside on
[Github](https://github.com/cetyler/openweather_report/wiki) in the wiki.
The [README](https://github.com/cetyler/openweather_report/blob/main/README.md)
will also include some of the initial documentation until it is necessary to
have a dedicated, detailed documentation.

### User Requirements

The initial requirements will be based on what I would like this program to do.
The
[wiki](https://github.com/cetyler/openweather_report/wiki/User-Requirements)
will have more detail, but I will describe at a high level what is in the User
Requirements.
User requirements go through and list what are the requirements that the
program should be able to do.
User requirements don't go into details in terms of what programming language,
software, etc. to use unless it is an absolute requirement.

The program should have the ability to pull data using [OpenWeather's
API](https://openweathermap.org/api).
The data should be able to save to either a file or database.
My requirements that the data should be saved to
[PostgreSQL](https://www.postgresql.org/) due to how much I use PostgreSQL at
work.
Optionally the data should be able to save to
[SQLite](https://www.sqlite.org/index.html) because it would be easier to share
the data since it would be a single file.

The program should be able to provide some reporting capabilities.
The program should have the option to display the last recorded values, the
forecast and historical data.

The goal of the program is to save the data and report the data initially in a
simplified format.
In the future the reporting can get more complex and have a robust interface.

### Design Requirements

The initial design requirements are how I would like to structure the program,
which programming language to use, etc.
The
[wiki](https://github.com/cetyler/openweather_report/wiki/Design-Requirements)
will have more detail but I would like describe at a high level here similar to
what I did for the User Requirements.
Due to this programming being used as a learning tool, it will be coded in
Python.
The design should be setup to use as either a standalone program or the ability
to import as a library.

#### Pulling OpenWeather Data

This should be straight forward since the data will be saved into the database
as a JSON column.
The [One Call API](https://openweathermap.org/api/one-call-3) JSON format won't 
be checked as the data being saved will be considered raw data.
I define raw data as data that is minimally modified from the source.
The data will then be saved either a text file or a database (SQLite and
PostgreSQL).
When that data is being saved to a database, there should at least an entry
date, what type of API call and the raw data.

At least initially, error checking will be minimal.
Testing will be minimal initially as well, though the goal is to have at least
all critical sections of the code tested.

The config file will store the following:

* API key required for OpenWeather.
* PostgreSQL login information.
* SQLite file location.
* Folder location to save text files.
* Default save type (PostgreSQL, SQLite, text).
* City information.

    * Longitude.
    * Latitude.
    * City ID from OpenWeather.

The program should be able to run using a cron job or if in Windows Task
Scheduler.

#### Displaying/Reporting Data

Initially it will be very basic.
For files, just return the JSON in a pretty format.
For databases, initially will support returning the data by entry date and
return the JSON in a pretty format.

The more complicated reports such as current conditions, forecast and
historical data, will prefer to do as much of the calculations in SQL if
possible.
The plan is to use [SQLAlchemy](https://www.sqlalchemy.org/) so that I can
learn how to use an ORM instead of doing raw SQL.

Testing and error checking here will much more robust than pulling in the data.
Logging probably is not needed since at least initially will not be run using a
cron job.

## Roadmap

Instead of creating a file or using the wiki, I will use utilize 
[Github Projects](https://github.com/cetyler/openweather_report/projects) as my
Roadmap.
Each project will be a major release (1.0.0, 2.0.0, etc.).
Each [milestone](https://github.com/cetyler/openweather_report/milestones) will 
be a minor or bug fix release.
The goal is to have a living Roadmap that shouldn't go out of date.

### Initial Release

Be able to pull data from OpenWeather using their One Call API.
Initially be able to save to a text file or to a database.

### Basic Displaying the Data

Be able to return results by location, date and data type.
The results will be displayed in the console.

### Basic Reporting

Be able to save a report to file or display the report.

### Basic Logging/Testing

Make sure that all critical areas of the code is tested.
Add some logging capabilities to note when there is an error.

### 1.0.0 Release

This release should have the features above as well as documentation.

### Interactive Display

Be able to display a dashboard to show current weather conditions and forecast.
Should have the option to export the report.

### Add Display API

Be able to use program as a library and do an API call to pull data from the
database to use for dashboards.


## Next Steps

The requirements and initial Roadmap is complete.
Will now work on using Github's project management features and start doing
some actual coding.
