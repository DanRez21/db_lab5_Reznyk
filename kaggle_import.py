import psycopg2 
import matplotlib.pyplot as plt
import csv
import pandas as pd

username = 'postgres'
password = '7256'
database = 'postgres'
host = 'localhost'
port = '5432'

# Connect to PostgreSQL
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
# Create a cursor
cur = conn.cursor()

csv_file = 'lb5\wine.csv'

def add_taster_id(input_file, output_file):
    
    df = pd.read_csv(input_file, on_bad_lines = 'skip')
    taster_id_map = {}
    current_id = 1

    for taster in df['taster_name'].unique():
        taster_id_map[taster] = current_id
        current_id += 1

    df['taster_id'] = df['taster_name'].map(taster_id_map)
    
    df.to_csv(output_file, index=False)

# Replace 'input.csv' and 'output.csv' with your actual file names
add_taster_id(csv_file, 'wine_r.csv')
df = pd.read_csv('wine_r.csv', on_bad_lines = 'skip')

query_1 = '''
    INSERT INTO Taster (taster_id, taster_name, taster_twitter_handle)
    VALUES (%s, %s, %s)
'''
query_2 = '''
    INSERT INTO Evaluation (eva_id, points, taster_id)
    VALUES (%s, %s, %s);
'''
query_3 = '''
    INSERT INTO Wine (wine_id, description, points, price, title, variety, eva_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
'''
query_4 = '''
    INSERT INTO location_ (location_id, country, designation, province, region_1, region_2, winery, wine_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
'''

query_5 = '''
DELETE FROM Taster
'''
query_6 = '''
DELETE FROM Evaluation
'''
query_7 = '''
DELETE FROM Wine
'''
query_8 = '''
DELETE FROM location_
'''

queries = (query_1, query_2, query_3, query_4)

with open('wine_r.csv', 'r') as file:

    cur.execute(query_8)
    cur.execute(query_7)
    cur.execute(query_6)   
    cur.execute(query_5)  
    reader = csv.DictReader(file)

    tasters = []
    for idx, row in enumerate(reader):
        print(idx)
        if idx < 10:
            if row['taster_id'] not in tasters:
                values = (row['taster_id'], row['taster_name'], row['taster_twitter_handle']) 
                cur.execute(query_1, values)
                tasters.append(row['taster_id'])

            values = (idx + 1, row['points'], row['taster_id']) 
            cur.execute(query_2, values)

            values = (idx + 1, row['description'], row['points'], row['price'], row['title'], row['variety'], idx + 1) 
            cur.execute(query_3, values)
            print(row)
            values = (idx + 1, row['country'], row['designation'], row['province'], row['region_1'], row['region_2'], row['winery'], idx + 1) 
            cur.execute(query_4, values) 
        else:
            break


    conn.commit()