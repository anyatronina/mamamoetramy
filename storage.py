import sqlite3
import json


conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS messagetaglist (message text, tag text)""")

conn.commit()
cursor.close()
conn.close()


def get_connection():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    return conn, cursor


def get_messages():
    _, cursor = get_connection()
    result = []
    for row in cursor.execute("SELECT message, tag from messagetaglist"):
        result.insert(0, {"message": row[0],
                          "tag": row[1]})
    return result
