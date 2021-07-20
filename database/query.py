import psycopg2
from database.conf_parser import config
from database.connect_db import connect


def insert_expenses(data_list):
    sql = """INSERT INTO expenses(id, category, sum, date)
            VALUES (%s, %s, %s, %s)"""
    connect(sql, data_list)
