# -*- coding: utf-8 -*-
"""
    Контролер веб интерфейса бота
    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""
import re
import os

from flask import Flask, Blueprint, abort, request, make_response, url_for, render_template

from web import app
from web import cache

api = Blueprint('api', __name__)


@api.route('/index', methods=['GET'])
def index():

    return 1
