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
        config = BtceConfig
        btce = BtceApi(config)

        btce.active = 1

        print btce.get_depth()

        # trades = btce.get_trades()
        # for pair in config.PAIR:
        #     for row in trades[pair]:
        #         print row['price_currency']
