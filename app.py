# -*- coding: utf-8 -*-
from flask import Flask
from views import index_page, entry_page, create_entry_page, add_message

app = Flask(__name__)

app.add_url_rule('/', view_func=index_page)
app.add_url_rule('/entry/<key>', view_func=entry_page)
app.add_url_rule('/create', view_func=create_entry_page)
app.add_url_rule('/add_message', view_func=add_message, methods=['POST'])


if __name__ == '__main__':
    app.run()
