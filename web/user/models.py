# -*- coding: utf-8 -*-

from web.database import Model, SurrogatePK, db


class User(SurrogatePK, Model):

    __tablename__ = 'api_user'

    STATUS_ACTIVE = 1
    STATUS_BANNED = 0

    SCHEME_EGGER = 'egger'
    SCHEME_BCK = 'bck'

    email = db.Column(db.String(128), nullable=False, index=True)
    key = db.Column(db.String(150))
    secret = db.Column(db.String(150))
    app = db.Column(db.Text, nullable=False)
    firm = db.Column(db.Text, nullable=False)
    scheme = db.Column(db.String(64), nullable=False)
    status = db.Column(db.Integer, index=True)
