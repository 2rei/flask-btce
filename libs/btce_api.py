# -*- coding: utf-8 -*-
"""
    Библиотека для работы с api btc-e

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""
import hashlib
import string
import json
from console import app
from grab import Grab
from lxml import etree


class BtceApi(object):

    def __init__(self, const):
        self.const = const
        self.pair = self.const.PAIR

    def get_fee_url(self, pair):
        return "%s/%s/%s" % (self.const.GENERAL_URL, pair, self.const.FEE_URL)

    def get_ticker_url(self, pair):
        return "%s/%s/%s" % (self.const.GENERAL_URL, pair, self.const.TICKER_URL)

    def set_request(self, url, data=None):
        return_data = False

        if data:
            grab.setup(post=data)

        self.grab = Grab()
        try:
            self.grab.go(url)
        except Exception as e:
            app.logger.error(e)
            self.grab = Grab()
        else:
            return_data = self.grab

        return return_data

    def get_fee(self):
        data = {}

        for pair in self.pair:
            result = self.set_request(self.get_fee_url(pair))

            if result:
                result_body = json.loads(result.response.body)
                data[pair] = result_body['trade']

        if len(data) == 0:
            data = False

        return data

    def get_ticker(self):
        data = {}

        for pair in self.pair:
            result = self.set_request(self.get_ticker_url(pair))

            if result:
                data[pair] = json.loads(result.response.body)

        if len(data) == 0:
            data = False

        return data
