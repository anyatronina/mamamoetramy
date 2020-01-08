import sqlite3
import json


conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS messagetaglist (message text, tag text)""")

variant = [('hello from inside', 'hello')]
cursor.executemany("INSERT INTO messagetaglist (message, tag) values (?,?)", variant)


def add_message_into_bd(text, tag):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    another = [(str(text), str(tag))]
    cursor.executemany("INSERT INTO messagetaglist (message, tag) values (?,?)", another)


def get_messages():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    result = []
    for row in cursor.execute("SELECT message, tag from messagetaglist"):
        result.append({"message": row[0],
                       "tag": row[1]})
    return result
