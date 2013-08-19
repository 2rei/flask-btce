# -*- coding: utf-8 -*-
"""
    Консольное приложение для тестирования и отладки

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""

from libs.btce_api import BtceApi
from flask.ext.script import Command

from console.configs.btce import BtceConfig


class TestCommand(Command):

    def run(self):
        btce = BtceApi(BtceConfig)
        print btce.get_ticker()
