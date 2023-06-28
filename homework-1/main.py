"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv
import os

path_cd = os.path.join("north_data", "customers_data.csv")
path_ed = os.path.join("north_data", "employees_data.csv")
path_od = os.path.join("north_data", "orders_data.csv")

sql_insert_cd = 'INSERT INTO customer_data VALUES(%s, %s, %s)'
sql_insert_ed = 'INSERT INTO employees_data VALUES(%s, %s, %s, %s, %s, %s)'
sql_insert_od = 'INSERT INTO orders_data VALUES(%s, %s, %s, %s, %s)'

conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='46pgBuchDD'
    )

try:
    with conn:
        with conn.cursor() as cur:

            with open(path_cd, 'r', encoding='utf-8') as file:
                contents = csv.reader(file)
                next(contents)
                cur.executemany(sql_insert_cd, contents)

            with open(path_ed, 'r', encoding='utf-8') as file:
                contents = csv.reader(file)
                next(contents)
                cur.executemany(sql_insert_ed, contents)

            with open(path_od, 'r', encoding='utf-8') as file:
                contents = csv.reader(file)
                next(contents)
                cur.executemany(sql_insert_od, contents)
finally:
    conn.close()