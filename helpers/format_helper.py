# -*- coding: utf-8 -*-
"""
    Хелпер для форматирования данных

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""

import decimal

from console.configs.btce import BtceConfig

decimal.getcontext().rounding = decimal.ROUND_DOWN
exps = [decimal.Decimal("1e-%d" % i) for i in range(16)]


def truncateAmountDigits(value, digits):
    quantum = exps[digits]
    return decimal.Decimal(value).quantize(quantum)


def truncateAmount(value, pair):
    return truncateAmountDigits(value, BtceConfig.MAX_DIGITS[pair])


def formatCurrencyDigits(value, digits):
    s = str(truncateAmountDigits(value, digits))
    dot = s.index(".")
    while s[-1] == "0" and len(s) > dot + 2:
        s = s[:-1]

    return s


def formatCurrency(value, pair):
    return formatCurrencyDigits(value, BtceConfig.MAX_DIGITS[pair])
