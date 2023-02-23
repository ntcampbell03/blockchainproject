from blockchainJson import *
from config import *
import math
import random
import jsonpickle

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
        for i in range(self.getNodeCount()-count+1):
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
        # return random.randint(1, self.getNodeCount())
        return 1 # TODO *+*+*+*+*+*+*+*+*+*+*

    def getNode(self, index=1):
        conn = get_db_connection()
        cur = conn.cursor()
        postgreSQL_select_Query = "select * from blockchain where id = (%s)"%(index,)
        cur.execute(postgreSQL_select_Query)
        print(index)
        bcjson = cur.fetchall()[0][1]
        cur.close()
        conn.close()
        return jsonpickle.decode(bcjson)

    def generateNodeList(self):
        res = []
        for i in range(math.ceil(self.userCount / CONFIG['nodes']['frequency'])-1):
            res.append(self.getNode(i+1))
        return res        
        
    def syncCalc(self, remove):
        verifiedChains = {}
        pendingTrans = []
        temp = []
        clen = 0
        longestChain = Blockchain(True)
        i = 1
        for chain in self.generateNodeList():
            if chain.verifyBlockchain():
                verifiedChains[i] = [chain, True]
                if chain.length > clen:
                    longestChain = chain
                    clen = longestChain.length
            else:
                verifiedChains[i] = [chain, False]
            for newTransaction in chain.newTransactions:
                if newTransaction.transactionString not in temp:
                    pendingTrans.append(newTransaction)
                    temp.append(newTransaction.transactionString)
            i+=1
        longestChain.newTransactions = pendingTrans
        if remove:
            longestChain.newTransactions = [remove]
        # print(verifiedChains)  // can implement later for visuals and shi
        return longestChain

    def syncChain(self, remove=None):
        conn = get_db_connection()
        cur = conn.cursor()
        longestJson = jsonpickle.encode(self.syncCalc(remove))
        for i in range(self.getNodeCount()):
            print("ENTERED LOOP")
            cur.execute('DELETE FROM blockchain WHERE id={}'.format(i+1))
            cur.execute('INSERT INTO blockchain (id, json)'
                        'VALUES (%s, %s)',
                        (i+1, longestJson)
                        )
            conn.commit()

        cur.close()
        conn.close()