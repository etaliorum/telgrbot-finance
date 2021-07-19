import psycopg2
from database.conf_parser import config


def insert_expenses(id, category, amount, date):
    sql = """INSERT INTO expenses(id, category, sum, date)
            VALUES (%s, %s, %s, %s)"""
    conn = None

    print(id)
    print(category)
    print(amount)
    print(date)

    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (id, category, amount, date,))
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')