+++
title = "Weather Project"
date = 2022-07-19T20:00:00-05:00
tags = ['python', 'project']
author = "Christopher Tyler"
summary = "Create a simple weather project to document how to add projects to PyPi and to aid with data analysis."
series = ["Weather Project"]
draft = false
+++

## Series

{{< series "Weather Project" >}}


## Overview

I haven't added anything to PyPi.
I wanted something to help generate data so that I can work on my data
analysis.
This article will cover what my requirements and goals are for this project.

## Requirements

I have three requirement sections:

- The weather program itself.
- Data analysis.
- Evaluating and updating Python workflow.

### Weather Program

I will go in more detail when I actually create the User Requirements but for
now I want to provide some high level requirements.
The program should be able to run using a scheduler like cron in Linux or the
Windows Scheduler.
This will enable getting data over time.
I want to use weather data from [OpenWeather](https://openweathermap.org/)
since I would like to try their 
[One API Call](https://openweathermap.org/api/one-call-3).
I also would like to save the data to [PostgreSQL](https://www.postgresql.org/)
to practice using PostgreSQL since I use PostgreSQL quite a bit at work.
Eventually it would nice that this program to set everything with in the
program itself.

### Data Analysis

I know I could go to websites like [Kaggle](https://www.kaggle.com/) but I
think it is more interesting getting data that I am actually interested in.
Obviously I can't use any data from work.
I also would like to practice with forecasting and while I could use stock
data, I think weather data would be a nice start.
I will have historical data to compare to and the forecast data from
OpenWeather.
I could see how accurate my forecast is as well as OpenWeather's forecast.
Then I can create dashboards to view and analyze the data.

### Python Workflow

I would like to evaluate my current workflow and use this project to continue
to make improvements.
I am currently evaluating [Pycharm](https://www.jetbrains.com/pycharm/) at work
while I am evaluating [Coder](https://github.com/coder/code-server) at home.

## Roadmap

I will include a roadmap in the project but I want to do a very high level
initial roadmap to get a minimal viable product.

- Create initial PyPi release to lock in project name.
- Create User Requirements.
- Create Design Requirements.
- Create README.
- Create Roadmap.
- Create tests.
- Create initial release.
- Review remaining roadmap and continue through the roadmap.

My plan unlike the Calculator Project is to continue to create article as I
work on this weather project.

## Next Steps

I will create a bare bones project so that I can lock in the project name on
[PyPi](https://pypi.org/).
I also want to be able to publish to TestPyPI as well as PyPi without needing
to input my username and password each time.
