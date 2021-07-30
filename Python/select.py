from login import cur

cur.execute("SELECT name,executed,updated FROM tablename")
res = cur.fetchall()

for i in res:
    print(i)
