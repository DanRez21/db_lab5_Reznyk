import csv
import os
import psycopg2 
import pandas as pd

username = 'postgres'
password = '7256'
database = 'postgres'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


def export_table_to_csv(connection, table_name):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    data = cur.fetchall()

    cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
    columns = [column[0] for column in cur.fetchall()]

    csv_file_path = f"{table_name}.csv"
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        csv_writer.writerow(columns)
        
        csv_writer.writerows(data)

def export_all_tables_to_csv(connection):
    cur = conn.cursor()

    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tables = cur.fetchall()

    for table in tables:
        table_name = table[0]
        export_table_to_csv(conn, table_name)

export_all_tables_to_csv(conn)
conn.close()