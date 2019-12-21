# -*- coding: utf-8 -*-
from collections import namedtuple

from flask import render_template, redirect, url_for, request

Message = namedtuple('Message', 'text')
messages = []


def entry_page(key):
    return render_template('entry.html', messages=messages)


def add_message():
    text = request.form['text']
    messages.append(Message(text))
    return redirect(url_for('entry/<key>'))
