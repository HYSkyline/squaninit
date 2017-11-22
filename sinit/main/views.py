# -*- coding:utf-8 -*-

from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/<username>')
def view(username):
    return render_template('userview.html', username=username)
    