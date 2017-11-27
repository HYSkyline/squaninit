# -*- coding:utf-8 -*-

from flask import current_app
from . import db


class sts(db.Model):
	__tablename__ = 'stable'
	id = db.Column(db.Integer, primary_key=True)
	sname = db.Column(db.String(16))
	sage = db.Column(db.Integer)
