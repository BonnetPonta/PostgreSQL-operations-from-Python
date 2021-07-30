from login import con, cur

sql = "INSERT INTO tablename (name) VALUES (%s)"
SET_NAMES = ["test"]
for SET_NAME in SET_NAMES:
    cur.execute(sql, (SET_NAME,))

con.commit()
