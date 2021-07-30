from login import cur, con

sql = "DELETE FROM tablename WHERE id = %s"
ID = 10
cur.execute(sql,(ID,))

con.commit()
