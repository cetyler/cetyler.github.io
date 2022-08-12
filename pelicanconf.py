#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = "Christopher Tyler"
SITENAME = "Christopher Tyler R&D Test Engineer"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Chicago"

DEFAULT_LANG = "en"

THEME = "pelican-themes/elegant"

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PLUGIN_PATHS = ["pelican-plugins"]

from pelican_jupyter import markup as nb_markup

PLUGINS = [
    "i18n_subsites",
    "sitemap",
    nb_markup,
    'tipue_search',
    'series',
]

DIRECT_TEMPLATES = [
        'search', 
        'index', 
        'archives',
        'authors',
        #'feeds',
        #'sitemap',
        'tags',
        'categories',
        #'archives',
        '404',
        ]

BIND = ""

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None #'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Automate the Boring Stuff", "https://automatetheboringstuff.com/"),
    ("Practical Business Python", "https://pbpython.com"),
    ("Real Python", "https://realpython.com"),
    ("Talk Python to Me", "https://talkpython.fm/"),
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/christopheretyler"),
    ("GitHub", "https://github.com/cetyler"),
    ("RSS", "https://cetyler.github.io/feeds/all.atom.xml"),
)

DEFAULT_PAGINATION = 10

# Sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 1,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {"articles": "always", "indexes": "hourly", "pages": "monthly"},
}

# Jupyter Notebook
MARKUP = ("md", "ipynb")

IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_MARKUP_USE_FIRST_CELL = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Default articles to draft
DEFAULT_METADATA = {
    "status": "draft",
}

# Comments
UTTERANCES_REPO = "cetyler/cetyler.github.io"
UTTERANCES_LABEL = "Comments"
UTTERANCES_FILTER = False
UTTERANCES_THEME = "github-light"

COMMENTS_INTRO = "Leave your comments below."

STATIC_PATHS = ["extra/robots.txt"]

EXTRA_PATH_METADATA = {"extra/robots.txt": {"path": "output/robots.txt"}}

SERIES_TITLE = "More in This Series"

# Legal
SITE_LICENSE = f"""
&copy; Copyright {date.today().year} by Christopher E. Tyler and licensed under a <a rel="license"
  href="http://creativecommons.org/licenses/by/4.0/">
  <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" />
  Creative Commons Attribution 4.0 International License</a>.
"""
