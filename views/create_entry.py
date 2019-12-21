# -*- coding: utf-8 -*-
from flask import request, render_template, redirect, url_for


def create_entry_page():
    '''if request.method == 'POST':
        article_name = request.form.get('article_name')
        return render_template('entry.html')'''
    return render_template('create_entry.html')
