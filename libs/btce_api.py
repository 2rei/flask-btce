# -*- coding: utf-8 -*-
"""
    Библиотека для работы с api btc-e

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""
import hmac
import hashlib
import string
import json
import time
import urllib

from grab import Grab

from console import app
from helpers.format_helper import *


class BtceApi(object):

    def __init__(self, const):
        self.grab = None
        self.result_count = 100
        self.result_start = 0
        self.result_active = 1
        self.nonce = int(time.time())
        self.const = const
        self.pair = self.const.PAIR
        self.public_method = self.const.PUBLIC_METHOD
        self.private_method = self.const.PRIVATE_METHOD

    def set_request(self, url, post=None, headers=None):
        return_data = False

        if not self.grab:
            self.grab = Grab()

        if post:
            self.grab.setup(post=post)

        if headers:
            self.grab.setup(headers=headers)

        try:
            self.grab.go(url)
        except Exception as e:
            app.logger.error(e)
        else:
            return_data = self.grab

        return return_data

    def _sign(self, post):
        post = urllib.urlencode(post)

        H = hmac.new(self.const.SECRET, digestmod=hashlib.sha512)
        H.update(post)

        return H.hexdigest()

    def _private_post(self, params):
        params['nonce'] = self.nonce

        headers = {
            'Key': self.const.KEY,
            'Sign': self._sign(params)
        }

        return self.set_request(self.const.PRIVATE_URL, params, headers)

    def _private_info(self, params):
        return_data = False
        result = self._private_post(params)

        if result:
            data = json.loads(result.response.body)
            if int(data['success']) == 1:
                return_data = data['return']

        return return_data

    def get_public_url(self, method):
        pair = '-'.join(self.pair)
        return "%s/%s/%s" % (self.const.PUBLIC_URL, method, pair)

    def _public_info(self, method):
        data = {}

        result = self.set_request(self.get_public_url(method))
        if result:
            data = json.loads(result.response.body)

        if len(data) == 0:
            data = False

        return data

    def get_info(self):
        return self._public_info(self.public_method['info'])

    def get_ticker(self):
        return self._public_info(self.public_method['ticker'])

    def get_trades(self):
        return self._public_info(self.public_method['trades'])

    def get_depth(self):
        return self._public_info(self.public_method['depth'])

    def get_user_info(self):
        params = {
            'method': self.private_method['user_info']
        }
        return self._private_info(params)

    def get_trans_history(self):
        params = {
            'method': self.private_method['trans_history'],
            'count': self.result_count,
            'from_id': self.result_start,
        }
        return self._private_info(params)

    def get_trade_history(self, pair=None):
        params = {
            'method': self.private_method['trade_history'],
            'count': self.result_count,
            'from_id': self.result_start,
        }
        if pair:
            params['pair'] = pair

        return self._private_info(params)

    def get_order_list(self, pair=None):
        params = {
            'method': self.private_method['order_list'],
            'count': self.result_count,
            'from_id': self.result_start,
            'active': self.result_active
        }
        if pair:
            params['pair'] = pair

        return self._private_info(params)

    def cancel_order(self, order_id):
        params = {
            'method': self.private_method['cancel_order'],
            'order_id': order_id,
        }

        return self._private_info(params)

    def trade(self, pair, trade_type, rate, amount):
        params = {
            'method': self.private_method['trade'],
            'pair': pair,
            'type': trade_type,
            'rate': rate,
            'amount': amount,
        }

        return self._private_info(params)
