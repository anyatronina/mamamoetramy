import sqlite3


def commit_after_execute(conn):
    def function(f):
        def wrapper(*args, **kwargs):
            f(*args, **kwargs)
            conn.commit()
        return wrapper
    return function


conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE users (user_id integer, user_name text)""")
cursor.execute("""INSERT INTO users VALUES (1, "Иван")""")


@commit_after_execute(conn)
def func(user):
    cursor.execute("""INSERT INTO users (user_id, user_name) VALUES(?, ?)""", user)


func((2, "Мария"))
cursor.execute("""SELECT * FROM users""")
print(cursor.fetchall())
