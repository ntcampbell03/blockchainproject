import json
from blockchainJson import *
from nodedistributor import *
import gnupg
import os

# blockchain1 =  Blockchain()
# blockchain1.writeChain()
# print(blockchain1.chain)

# da = NodeDistributor()
# da.test()

def get_db_connection():
    conn = psycopg2.connect(user="xpahdelqnuopvl",
                    password="edcc7b324dd36ca1f59a3849bf503c52e1e3499cd64835f88ad7f96401d3d31c",
                    host="ec2-100-26-39-41.compute-1.amazonaws.com",
                    port="5432",
                    database="d8lbeqdtcsvnma")
    return conn


conn = get_db_connection()
cur = conn.cursor()
print("WRITING1")
cur.execute('ALTER TABLE blockchain ADD PRIMARY KEY (id);')

cur.close()
conn.close()

