import psycopg2

def createTable():
    conn = psycopg2.connect(
        "dbname='data2' user='postgres' password='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("Create TABLE data(rollNo INTEGER ,name TEXT,marks REAL)")
    conn.commit()
    conn.close()


def insert(rollNo, name, marks):
    conn = psycopg2.connect(
        "dbname='data2' user='postgres' password='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)", (rollNo, name, marks))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data ")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(roll):
    conn = psycopg2.connect("dbname='data2' user='postgres' password='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE rollNo=%s", (roll,))
    conn.commit()
    conn.close()


print(view())
delete(5)
print(view())