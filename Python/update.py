from login import con, cur

EXECUTED = 'hoge'
NAME = 'hoge'


def update(EXECUTED, NAME):
    sql = "UPDATE tablename SET executed = %s WHERE name = %s"
    cur.execute(sql, (EXECUTED, NAME))

    con.commit()


update(EXECUTED, NAME)
