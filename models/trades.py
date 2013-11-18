# -*- coding: utf-8 -*-
"""
    Модель операций покупки и продажи

    :copyright: (c) 2013 by Pavel Lyashkov.
    :license: BSD, see LICENSE for more details.
"""
from web import db, app


class Trades(db.Model):

    __bind_key__ = 'btce'
    __tablename__ = 'trades'

    TYPE_BID = 0
    TYPE_ASK = 1

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False, index=True)
    price = db.Column(db.String(300), nullable=False)
    amount = db.Column(db.String(300), nullable=False)
    pair = db.Column(db.Integer, nullable=False, index=True)

    def __repr__(self):
        return '<id %r>' % (self.id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app.logger.error(e)
            return False
        else:
            return True
