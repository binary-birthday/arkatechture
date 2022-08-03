import csv
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()
conn = None

try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        port=os.getenv('POSTGRES_PORT')
    )

    cur = conn.cursor()

    def get_files_with_ext(directory, file_ext=".csv"):
        filenames = os.listdir(directory)
        return [filename for filename in filenames if filename.endswith(file_ext)]

    def read_file_and_insert_into_db(filename, files):
        files.index(filename)
        table_name = "products" if "Product" in filename else "salespeople" if "people" in filename else "sales"
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)
            for row in reader:
                cur.execute(
                    sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                        sql.Identifier(table_name),
                        sql.SQL(', ').join(map(sql.Identifier, headers)),
                        sql.SQL(', ').join(sql.Placeholder() * len(row)),
                    ), row
                )
        conn.commit()

    try:
        files = get_files_with_ext(os.getcwd())
        num_files = len(files)
        if num_files != 3:
            raise Exception("Expected three files, found %s files", num_files)
        else:
            read_file_and_insert_into_db("ProductData.csv", files)
            read_file_and_insert_into_db("SalespeopleData.csv", files)
            read_file_and_insert_into_db("SalesData.csv", files)
    except Exception as e:
        print(e)

    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
