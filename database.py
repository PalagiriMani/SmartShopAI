import sqlite3

def get_db():
    conn = sqlite3.connect("smartshop.db")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.executescript(open("data/init_data.sql").read())
    conn.commit()
    conn.close()
