import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm.session import sessionmaker

import psycopg2
import logging

def get_db_connection():
    PGHOST = os.getenv("DB_HOST","localhost")
    PGDATABASE = "postgres"
    PGUSER = "postgres"
    PGPASSWORD = ""
    PGPORT = "5432"
    conn_string = "postgresql://" + PGUSER + PGPASSWORD + "@" + PGHOST + ":" + PGPORT + "/" + PGDATABASE

    conn = psycopg2.connect(conn_string)
    return conn

def test_sql():

    conn = get_db_connection()
    cursor = conn.cursor()

    #cursor.execute('SELECT * from ')
    #row = cursor.fetchone()

    #conn.close()
