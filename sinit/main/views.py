# -*- coding:utf-8 -*-

from flask import render_template
from . import main
from .. import db
from ..models import sts


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/auth/<username>')
def view(username):
    return render_template('userview.html', username=username)


@main.route('/get')
def sts_view():
	stss = sts.query.all()
	return render_template('get.html', sts = stss)
