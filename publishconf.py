#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://changyuheng.github.io'
RELATIVE_URLS = False

SITESEARCH = 'https://google.com/search'
SITESEARCHFILTER = 'changyuheng.github.io'

FEED_DOMAIN = 'http://' + SITESEARCHFILTER
FEED_ATOM =  'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_RSS = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "aprogrammersblog"
GOOGLE_ANALYTICS = "UA-44162683-1"

GITHUB_URL = 'https://github.com/changyuheng'