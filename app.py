from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request
from storage import get_messages, get_connection


app = Flask(__name__)

Message = namedtuple('Message', 'text tag')


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    messages = get_messages()
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    message = request.form['text']
    tag = request.form['tag']
    conn, cursor = get_connection()
    cursor.execute("INSERT INTO messagetaglist (message, tag) values (?,?)", (message, tag))
    conn.commit()
    return redirect(url_for('main'))


@app.route('/get_all_messages', methods=['POST'])
def get_all_messages():
    conn, cursor = get_connection()
    cursor.execute("SELECT message, tag FROM messagetaglist")
    f = open('all_messages.txt', 'w')
    records = cursor.fetchall()
    for row in records:
        f.write(row[0] + ' # ' + ' #'.join(row[1].split(',')) + '\n')
    f.close()
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()
