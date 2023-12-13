import psycopg2
import json

username = 'postgres'
password = '7256'
database = 'postgres'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


def export_all_tables_to_json(conn):
    cursor = conn.cursor()
    tables = ['taster', 'evaluation', 'location_', 'wine']

    data_dict = {}

    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        table_data = cursor.fetchall()
        all_data = []

        columns = [i[0] for i in cursor.description]
        for row in table_data:
            all_data.append(dict(zip(columns, row)))

        data_dict[table] = all_data

    cursor.close()
    conn.close()

    with open('output.json', 'w') as json_file:
        json.dump(data_dict, json_file)

export_all_tables_to_csv(conn)