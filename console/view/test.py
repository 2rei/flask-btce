# -*- coding: utf-8 -*-
"""
    Консольное приложение для тестирования и отладки

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""
import random
from flask.ext.script import Command


class TestCommand(Command):

    def rate(self, count, all):
        data = range(1, all + 1)
        random.shuffle(data)
        rate = sorted(random.sample(data, count))

        return rate

    def run(self):
        print self.rate(5, 36)
        print self.rate(6, 45)
        print self.rate(7, 49)
