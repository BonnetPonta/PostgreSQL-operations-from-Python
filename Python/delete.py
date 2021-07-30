from login import cur, con

sql = "DELETE FROM tablename WHERE id = %s"
IDS = 10
for ID in IDS:
    cur.execute(sql,(ID,))

con.commit()
