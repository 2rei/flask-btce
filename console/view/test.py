# -*- coding: utf-8 -*-
"""
    Консольное приложение для тестирования и отладки

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""

import time
from libs.btce_api import BtceApi
from flask.ext.script import Command

from console.configs.btce import BtceConfig

from models.trades import Trades
from web import db


class TestCommand(Command):

    def run(self):

        config = BtceConfig
        btce = BtceApi(config)
        pairs = BtceConfig.PAIR
        min_orders = BtceConfig.MIN_ORDERS

        btce.active = 1

        trades = btce.get_trades()

        for key in pairs:
            for row in trades[key]:
                if row['amount'] < min_orders[key]:
                    continue

                trade = Trades.query.get(row['tid'])
                if trade:
                    continue

                trade = Trades()
                trade.id = row['tid']
                trade.date = row['timestamp']
                trade.type = Trades.TYPE_BID if 'bid' in row[
                    'type'] else Trades.TYPE_ASK
                trade.price = row['price']
                trade.amount = row['amount']
                trade.pair = pairs[key]

                db.session.add(trade)

        db.session.commit()
