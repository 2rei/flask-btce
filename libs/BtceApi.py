# -*- coding: utf-8 -*-
"""
    Библиотека для работы с api btc-e

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""
import hashlib
import string
import csv
from console import app
from grab import Grab
from lxml import etree


class BtceApi(object):
