import csv
import psycopg2

conn = None

try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host="db",
        database="postgres",
        user="postgres",
        password="postgres",
        port="5432")

    cur = conn.cursor()

    files = ['ProductData.csv', 'SalesmanData.csv', 'SalesData.csv']

    for file in files:
        if file == 'ProductData.csv':
            with open(file) as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  # Skip the header row.
                for row in reader:
                    cur.execute(
                        "INSERT INTO products (product_id, product_name, unit_price) VALUES (%s, %s, %s)",
                        row
                    )
                    conn.commit()
        elif file == 'SalesmanData.csv':
            with open(file) as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  # Skip the header row.
                for row in reader:
                    cur.execute(
                        "INSERT INTO salespeople (salesperson_id, salesperson_name) VALUES (%s, %s)",
                        row
                    )
                    conn.commit()
        elif file == 'SalesData.csv':
            with open(file) as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  # Skip the header row.
                for row in reader:
                    cur.execute(
                        "INSERT INTO sales (customer_name, salesperson_id, product_id, quantity_sold, sale_date) VALUES (%s, %s, %s, %s, %s)",
                        row
                    )
                    conn.commit()
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
