
import psycopg2
from psycopg2 import Error
import json

conn = psycopg2.connect(user="xpahdelqnuopvl",
                        password="edcc7b324dd36ca1f59a3849bf503c52e1e3499cd64835f88ad7f96401d3d31c",
                        host="ec2-100-26-39-41.compute-1.amazonaws.com",
                        port="5432",
                        database="d8lbeqdtcsvnma")

def init_bc():
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute('DROP TABLE IF EXISTS blockchain;')
    cur.execute('CREATE TABLE blockchain (id INTEGER, json TEXT);')

    # Insert data into the table
    with open('blockchain.json', 'r') as openfile:
                json_object = json.load(openfile)
                json_object = json.dumps(json_object)
    cur.execute('INSERT INTO blockchain (id, json)'
                'VALUES (%s, %s)',
                (
                1,
                json_object)
                )

    conn.commit()

    cur.close()
    conn.close()

def init_ac():
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute('DROP TABLE IF EXISTS user;')
    cur.execute('CREATE TABLE user (id INTEGER, json TEXT);')

    # Insert data into the table
    with open('blockchain.json', 'r') as openfile:
                json_object = json.load(openfile)
                json_object = json.dumps(json_object)
    cur.execute('INSERT INTO blockchain (id, json)'
                'VALUES (%s, %s)',
                (
                1,
                json_object)
                )

    conn.commit()

    cur.close()
    conn.close()
