from json import load

from psycopg2 import connect

with open("config.json", "r", encoding="utf-8_sig") as f:
    PostgreSQL_config = load(f)["PostgreSQL_config"]
    HOST = PostgreSQL_config["host"]
    PORT = PostgreSQL_config["port"]
    DBNAME = PostgreSQL_config["dbname"]
    USER = PostgreSQL_config["user"]
    PASSWORD = PostgreSQL_config["password"]

# connect
con = connect(
    f"host={HOST} port={PORT} dbname={DBNAME} user={USER} password={PASSWORD}"
)
cur = con.cursor()
