import sqlite3

def createTable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("Create TABLE data(rollno INTEGER ,name TEXT,marks REAL)")
    conn.commit()
    conn.close()


createTable()