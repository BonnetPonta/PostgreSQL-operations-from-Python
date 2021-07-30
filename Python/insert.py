from login import con, cur

sql = "INSERT INTO tablename (name) VALUES (%s)"
SET_NAME = "test"
cur.execute(sql, (SET_NAME,))

con.commit()
