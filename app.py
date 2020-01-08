from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request
from storage import add_message_into_bd, get_messages


app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = get_messages()


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    add_message_into_bd(text, tag)

    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()
