import psycopg2

con = psycopg2.connect(
    host = "localhost",
    database="mycooldb",
    user = "yli",
    password = "8765")

cur = con.cursor()

cur.execute("insert into people values(%s, %s, %s)", (6, 'Ali', 'Gates'))
#didn't see this record in pgadmin, has to commit your changes


cur.execute("select id, name from people")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name {[r[1]]}")

con.commit()
cur.close()


con.close()
