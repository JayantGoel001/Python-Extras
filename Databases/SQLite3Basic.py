import sqlite3


def createTable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("Create TABLE data(rollNo INTEGER ,name TEXT,marks REAL)")
    conn.commit()
    conn.close()


def insert(rollNo, name, marks):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)", (rollNo, name, marks))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data ")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(roll):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollNo=?", (roll,))
    conn.commit()
    conn.close()


def update(roll, name, mark):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=?,marks=? WHERE rollNo=?", (name, mark, roll))
    conn.commit()
    conn.close()


createTable()
insert(0, "JA", 0.92)
print(view())
delete(5)
print(view())
update(0, "Jai", 92)
print(view())
