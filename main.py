import psycopg2 
import matplotlib.pyplot as plt

username = 'postgres'
password = '7256'
database = 'postgres'
host = 'localhost'
port = '5432'

# Connect to PostgreSQL
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
# Create a cursor
cur = conn.cursor()

create_taster_points_view = """
    CREATE OR REPLACE VIEW taster_points AS
    SELECT taster_name, AVG(e.points) AS average_evaluation
    FROM wine w
    JOIN evaluation e ON w.eva_id = e.eva_id
    JOIN taster ta ON ta.taster_id = e.taster_id
    GROUP BY taster_name;
"""
cur.execute(create_taster_points_view)


create_countries_view = """
    CREATE OR REPLACE VIEW countries_view AS
    SELECT country, COUNT(*) AS wine_count
    FROM wine w
    JOIN location_ l ON w.wine_id = l.wine_id
    GROUP BY country;
"""
cur.execute(create_countries_view)


create_country_points_view = """
    CREATE OR REPLACE VIEW country_points AS
    SELECT AVG(e.points) AS average_evaluation, l.country 
    FROM wine w
    JOIN evaluation e ON w.eva_id = e.eva_id
    JOIN taster ta ON ta.taster_id = e.taster_id
    JOIN location_ l ON l.wine_id = w.wine_id
    GROUP BY l.country;
"""
cur.execute(create_country_points_view)


cur.close()

query_taster_points = "select * from taster_points;"
query_countries = "select * from countries_view;"
query_country_points = "select * from country_points;"

with conn:
    cur = conn.cursor()

    cur.execute(query_taster_points)
    taster_points = cur.fetchall()

    cur.execute(query_countries)
    countries = cur.fetchall()

    cur.execute(query_country_points)
    country_points = cur.fetchall()


    labels_a, values_a = zip(*taster_points)
    labels_b = [row[1] for row in countries]
    values_b = [row[0] for row in countries]
    values_c = [int(row[0]) for row in country_points]
    label_c = [str(row[1]) for row in country_points]


    fig, ax = plt.subplots(1, 3, figsize = (15, 5))


    ax[0].bar(labels_a, values_a, color = 'blue')
    ax[0].set_title('Number of Deaths by Method')
    ax[0].set_xlabel('Taster')
    ax[0].set_ylabel('Points')
    ax[0].set_ylim([70, 100]) 
    ax[0].set_title('Average points by taster')


    ax[1].pie(labels_b, labels=values_b, autopct='%1.1f%%', startangle=140)
    ax[1].set_title('Percentage of Wine Production')

    ax[2].plot(label_c, values_c, color = 'maroon')
    ax[2].bar(label_c, values_c, color = 'cyan')
    ax[2].set_xlabel('Points')
    ax[2].set_ylabel('Country')
    ax[2].set_title('Avarage Points in Countries')
    ax[2].set_ylim([70, 100]) 
    fig.savefig('graphs.png')

    plt.tight_layout()
    plt.show()
