import psycopg2

def createTable():
    conn = psycopg2.connect(
        "dbname='data2' user='postgres' password='postgres' password='postgres' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("Create TABLE data(rollNo INTEGER ,name TEXT,marks REAL)")
    conn.commit()
    conn.close()


createTable()
