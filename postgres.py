import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="pw1337", host="127.0.0.1", port="5432")

cur = conn.cursor()

cur.execute("""CREATE TABLE LUDZIKI (
                id      INT,
                name    TEXT,
                age     INT,
                color   TEXT
                )""")

cur.execute("""INSERT INTO USERS(id, name, age, color)
                VALUES (1, 'Zbigniew', 32, 'Mudzin')""")

cur.execute("""INSERT INTO USERS(id, name, age, color)
                VALUES (1, 'Endrju', 42, 'Bialas')""")


cur.execute("""SELECT id, name, age, color
             FROM users""")

# Fetch the data
rows = cur.fetchall()

# Do stuff with the data
for row in rows:
    print("ID = {}".format(row[0]))
    print("NAME = {}".format(row[1]))
    print("AGE = {}".format(row[2]))
    print("COLOR = {}".format(row[3]))


conn.commit()
conn.close()
