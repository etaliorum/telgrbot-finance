import psycopg2
from database.conf_parser import config
from database.connect_db import insert_db


def insert_expenses(data_list):
    sql = """INSERT INTO expenses(id, category, sum, date)
            VALUES (%s, %s, %s, %s)"""
    insert_db(sql, data_list)


def get_expenses(id):
    sql = """SELECT id, category, sum FROM expenses"""
    return None
