# -*- coding: utf-8 -*-
"""
   Входной скрипт

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""
from web import app
app.config.from_object('configs.general.DevelopmentConfig')
app.run(host='127.0.0.1', port=6000)
