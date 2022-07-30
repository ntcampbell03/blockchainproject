import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="xpahdelqnuopvl",
                                  password="edcc7b324dd36ca1f59a3849bf503c52e1e3499cd64835f88ad7f96401d3d31c",
                                  host="ec2-100-26-39-41.compute-1.amazonaws.com",
                                  port="5432",
                                  database="d8lbeqdtcsvnma")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE blockchain
          (ID INT PRIMARY KEY     NOT NULL,
          BLOCKCHAIN           TEXT    NOT NULL,
          PRICE         REAL); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")