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


insert(1, "Pugg Ms", 100.0)
