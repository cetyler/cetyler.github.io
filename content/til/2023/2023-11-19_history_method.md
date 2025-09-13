+++
title = 'See the History of a MEthod with git log -L'
date = 2023-11-19T23:56:35-05:00
draft = false
tags = ['Caleb Hearth','Simon Willison','git']
summary = "Saw this on Simon's blog."
comments = true
+++

Simon posted an [article](https://calebhearth.com/git-method-history) from
Caleb on a way to get the history of a method.

It works with Python out of the box:

```bash
git log -L :path_with_format:__init__.py
```

That command displays a log (with diffs) of just the portion of commits that
changed the path_with_format function in the `__init__.py` file.

**Note** that it doesn't appear to work with a method in a class so just get
the history of the class

```bash
> git log -L :OpenWeather:get_weather/openweather.py

commit a5c823508c27be6e47f07e692c457908216fe48d (HEAD -> main, tag: 1.1.1, origin/main)
Author: Christopher Tyler <christophertyler@proton.me>
Date:   Sun Mar 26 20:23:29 2023 -0500

    Release 1.1.0 (#40)
    
    # Overview
    
    Minor release to update some of the development tooling and do some minor
    features.
    
    # Features
    
    * Added: Application name to PostgreSQL connection string.
    * Added: Update to use Python 3.11 features.
    * Added: Command line option to get the software version.
    * Added: Software version to save in database.
    * Changed: Switch to standard library tomllib.
    * Changed: Removed json config file.
    * Changed: Switch from poetry to flit and pip-chill.
    
    Co-authored-by: Christopher Tyler <christophertyler@engineer.com>
    Co-authored-by: Christopher Tyler <ctyler@dmimail.com>
    Reviewed-on: http://192.168.0.113:3000/Personal/get_weather/pulls/40

diff --git a/get_weather/openweather.py b/get_weather/openweather.py
--- /dev/null
+++ b/get_weather/openweather.py
@@ -0,0 +29,96 @@
+class OpenWeatherMap:
+    """To interface with OpenWeatherMap's API.
+
+    This class will make API calls to get JSON data from OpenWeatherMap.
+    """
+
+    latitude: float = 0

...
```

