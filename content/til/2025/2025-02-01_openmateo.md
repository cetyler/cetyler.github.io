+++
title = 'Open Mateo Weather API'
date = 2025-02-01T19:22:40-06:00
draft = false
tags = ['open_mateo','python','weather','api']
summary = 'Open Mateo can be an alternative to Open Weather Map.'
comments = true
+++

[Open Mateo](https://open-meteo.com/) is an open source weather API that offers
free access for non-commercial use similar to
[Open Weather Map](https://openweathermap.org/).
The main difference is that Open Weather Map you have to sign up to get free
access and you are limited to 1,000 API calls per day.
Open Mateo will provide up to 10,000 API calls per day and doesn't appear to
require a sign up.
The other difference it appears that Open Mateo provides 
[historical data](https://openmeteo.substack.com/p/introducing-the-historical-forecast)
from 2021 and onwards. 

Will probably create an article once I have a chance to play with it.
[Using their documentation](https://open-meteo.com/en/docs), it will provide
example code when selecting what you are looking for from the API. 

## Install

```python
pip install openmeteo-requests
pip install requests-cache retry-requests numpy pandas
```

## Usage

```python
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"hourly": "temperature_2m"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}

hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)
```
