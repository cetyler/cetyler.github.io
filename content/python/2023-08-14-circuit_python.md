Title: Measure Ambient Conditions with Circuit Python
Date: 2023-08-20 20:00
Category: Python
Tags: python, circuit python, adafruit, feather board, esp32s2
Author: Christopher
Summary: Overview on Circuit Python using AdaFruit's Feather boards.
comment_id: circuit_python_ambient
Status: Published

## Overview

I have been meaning to try out [Circuit Python](https://circuitpython.org/) but
I didn't quite have a project in mind.
I had a janky setup using a Raspberry Pi, some thermistors and a
temperature/humidity sensor on a bread board to measure the input and output of
my air conditioner.
It was meant to be temporary but I ended up using it far after determining that
my air conditioner needed to be replaced.
I moved the setup which caused all the wires to popped out.
I also had a Sparkfun's
[Humidity Breakout Board](https://www.sparkfun.com/products/16467) but didn't
realized that they only had an Arduino library.
The plan was to compare the ambient conditions of my house relative to the
outside weather conditions.
Instead of trying to create a better setup with my existing parts, I decided to
use the opportunity start over.
I had the following requirements:

* Be able to measure conditions at multiple locations in my house.
* Be able to measure temperature and optionally humidity.
* Be able to send the data wirelessly to my PC.

This lead me to
[AdaFruit ESP32-S2 Feather](https://learn.adafruit.com/adafruit-esp32-s2-tft-feather)
(I got the one with [BME280 Sensor](https://www.adafruit.com/product/5303) and
using [Circuit Python](https://circuitpython.org).
This article will be less about the board and more about using Circuit Python.

## What is Circuit Python?

[MicroPython](https://micropython.org/) created a cutdown version of Python
that could run in microcontrollers.
[Circuit Python](https://circuitpython.org) is based on MicroPython and you can
see the differences
[here](https://docs.circuitpython.org/en/latest/README.html#differences-from-micropython).
[Many of AdaFruit boards](https://circuitpython.org/downloads) as well as
Raspberry Pis and other boards can be programmed with Circuit Python.

If you have used Python, most likely you used the
[CPython](https://github.com/python/cpython) implementation.
The differences between CPython and MicroPython/CircuitPython it is easier to
remember that CPython is not meant for microcontrollers.
CircuitPython and MicroPython have a much smaller standard library and may not
have all the features that CPython has (details
[here](https://github.com/micropython/micropython/wiki/Differences)).

## Setting Up to Use Circuit Python

AdaFruit has a good
[guide](https://learn.adafruit.com/welcome-to-circuitpython) which can be good
if you are new to microcontrollers as well as Python.
My workflow is currently the following:

* Code using [vim](https://www.vim.org/) or [Kate](https://apps.kde.org/kate/).
  * Sometimes will change the code directly on the board but usually will work
    in my Git repo.
* If I need an output, I use [screen](https://www.gnu.org/software/screen/)
  (ex. `screen /dev/ttyACM0 115200`).
* Remember to not keep to board connected to the PC if I want it to go to sleep.

When I got my board, I had to update it so that I could a) be able to have it
plug in to my PC and be treated as a USB drive and b) update to the latest
version of Circuit Python.
I used AdaFruit's
[Web Serial](https://adafruit.github.io/Adafruit_WebSerial_ESPTool/) though it
does require Chrome 89 or higher.
Keep in mind that AdaFruit does have documentation for
[specific boards](https://circuitpython.org/board/adafruit_feather_esp32s2/).

## AdaFruit Feather ESP32-S2

I mainly got [this board](https://www.adafruit.com/product/5303) because it
have BME280 temperature/humidity/pressure sensor.
AdaFruit does have [BME280](https://www.adafruit.com/product/2652) as a
separate board using their STEMMA QT connector.
The nice thing about AdaFruit is that they have great documentation and good
examples.
There is an
[example](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout)
on how to use BME280 sensor.

### Code Overview

Since the BME280 sensor is on the board, I found out that the board will heat
up enough to affect the readings.
I put the board asleep and on wake up, get the readings before turning on WiFi.
After the WiFi is turned on, I try and connect to my server to get the sea
level pressure.
Sea level pressure is required if I want to return the altitude.
Then the board will send temperature, humidity, pressure and altitude to my
server.
The board will go to sleep for 5 minutes.

My server gets the sea level pressure when I poll
[OpenWeatherMap](https://openweathermap.org/api/one-call-3).
The server keeps all the data in a [PostgreSQL](https://postgresql.org/)
database.

### Feather Board

The only libraries I needed to get was
[BME280](https://docs.circuitpython.org/projects/bme280/en/latest/index.html)
and
[requests](https://docs.circuitpython.org/projects/requests/en/latest/index.html).
The examples gave me a good start on how to use both libraries.
The rest of the libraries are part of Circuit Python and I didn't need to
download anything.
In `secrets.py`, I put my WiFi, board name and server info there.

I found getting multiple readings help ensure that I get an actual reading.
I don't do any averaging or comparing the readings though.
In the future, I may do some checks to compare the readings, throw out any
outliers and take an average.

I then turn on the WiFi and attempt to connect to make a connection.
If I am not successful, I sleep for a minute and try everything again.
If I am successful, I will then attempt to communicate with my server.

The board will try and get a sea level pressure reading.
If it fails for some reason, the board will use a default value of 1013.25 kPa.

I turn on the LED so that I know that my board is attempting to send data.
The board will try and send the readings to the server.
If it fails, will sleep for a minute and try everything again.
If successful, will sleep for 5 minutes.

As you can see it is a fairly basic program.
I plan on sharing the source once I do some cleaning up.
I also have boards with LCD screens but I need to figure out a way to display
the data when pressing one of the buttons.
That code will also eventually be shared.

### Server

I will briefly cover this but I use the following third party libraries:

* [aiosql](https://nackjicholson.github.io/aiosql/)
* [Flask](https://flask.palletsprojects.com/)
* [pyscopg2](https://www.psycopg.org/)

Using aiosql I can turn SQL code into a Python function, keeping my SQL and
Python code in separate files.
This is my first project using Flask and right now I am still using the
development server.
Before I attempt to share this, I will need to do some major cleaning of the
code.
I have some basic checks but it is still very much in an alpha state.
I basically have a couple of routes.
`board_data` is so that I can look at the last board that send data in a basic
JSON format.
`sea_level_data` is so that the boards can get the current sea level data for
my location.
In the future, I should support asking for a city instead of having it
hardcoded.
I would like to create a settings file so that I can remove some hardcoded
configuration and turn it into a [pipx](https://pypa.github.io/pipx/)
installable package.
I also would like to create a simple landing page that can show some stats like
the readings from the last 24hrs., latest readings for all active boards, etc.
Finally I would like the server to have an initialization step to setup the
PostgreSQL/[SQLite](https://www.sqlite.org/index.html) database before I think
about sharing the code.

## Next Steps

I will either update this article or add a more detailed article once I release
the board and server code.
However I was able to use AdaFruit excellent examples to create something that
has been working for the last 6 months or so.
My current board code is mostly a mashup of their examples to get something
working.

Similar to
[OpenWeather Report package](https://github.com/cetyler/openweather_report) I
created, I would like to clean up my code before I feel comfortable sharing.
I also would like to create some tests to build my habits creating tests much
earlier in the development.
I do have some boards with LCD screens that I would like experiment with either
using the button to get the current readings or see if an always on display can
work without affecting the readings.
My server probably need the most work as it is truly a minimal viable product
(MVP). I would like something that I could have some sort of dashboard or at
the very least be able to do some API calls to get data from my database.
