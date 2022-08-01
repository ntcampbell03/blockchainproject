from blockchainJson import *
from config import *
import math
import random

class NodeDistributor:
    def __init__(self):
        self.userCount = 0
        self.nodeCount = 0

    def setUserCount(self, userCount):
        self.userCount = userCount

    def getNodeCount(self):
        self.nodeCount = math.ceil(self.userCount / CONFIG['nodes']['frequency'])
        return self.nodeCount

    def provisionNode(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM blockchain')
        count = cur.fetchone()[0]
        cur.close()
        cur = conn.cursor()
        print(self.getNodeCount()-count)
        for i in range(self.getNodeCount()-count):
            print("ENTERED LOOP")
            postgreSQL_select_Query = "select * from blockchain where id = (1)"
            cur.execute(postgreSQL_select_Query)
            json_object = cur.fetchall()[0][1]
            cur.execute('INSERT INTO blockchain (id, json)'
                        'VALUES (%s, %s)',
                        (count+i+1, json_object)
                        )
            conn.commit()

        cur.close()
        conn.close()

    def randomNode(self):
        if self.userCount <= 1:
            return 1
        if self.nodeCount < math.ceil(self.userCount / CONFIG['nodes']['frequency']):
            self.provisionNode()
        return random.randint(1, self.getNodeCount())

    def test(self):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM user')
        count = cur.fetchone()[0]
        print(count)

        cur.close()
        conn.close()