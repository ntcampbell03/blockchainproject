from wallet import *
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = [self.GenesisBlock()]
        self.length = 1
        self.difficulty = 5
        self.newTransactions = []
        self.numTransactions = 0
        self.miningReward = 10

    def getBlock(self, n):
        return self.chain[n]

    def getLastBlock(self):
        return self.chain[-1]

    def addTransaction(self, transaction):
        try:
            print(transaction.amount)
            if transaction.sender.futureBalance >= transaction.amount:
                self.newTransactions.append(transaction)
                transaction.sender.futureBalance -= transaction.amount
                self.numTransactions += 1
                print('Transaction sucessfully added!')
            else:
                print('Wallet has insufficient balance!')
        except NameError:
            print('Wallet does not exist!') #Tryblockchain.addTransaction(t) except doesnt work
            
    def addBlock(self):
        if self.newTransactions:
            for transaction in self.newTransactions:
                if str(gpg.decrypt(str(transaction.signature), passphrase = transaction.reciever.name)) == transaction.transactionString:
                    print()
                    transaction.sender.sent += transaction.amount
                    transaction.reciever.recieved += transaction.amount
                    transaction.sender.getBalance()
                    transaction.sender.futureBalance = transaction.sender.futureBalance
                    transaction.reciever.getBalance()
                    transaction.reciever.futureBalance = transaction.reciever.futureBalance
            newBlock = Block(self.newTransactions, self.length, self.getLastBlock().hash)
            newBlock.mineBlock(self.difficulty)
            if self.getLastBlock().index <= newBlock.index:
                self.length += 1
                self.chain.append(newBlock)
                self.newTransactions = []
                self.numTransactions = 0
                return self.miningReward
        else:
            print("No pending transactions")
            return 0
        
    
    def verifyBlockchain(self):
        prevHash = '0'
        for curBlock in self.chain[1:]:
            if curBlock.hash != curBlock.calculateHash(): #Check if hash is legitimate
                print("Hash does not match data")
                return False
            for i in curBlock.hash[0:self.difficulty]: #Check if hash is acceptable
                if i != '0':
                    print("Hash does not meet requirements")
                    return False
            if curBlock.prev != prevHash: #Check if prev is acceptable
                print("Previous hash does not match")
                return False
            prevHash = curBlock.hash
            for transaction in curBlock.transactions: #Check if transaction signatures are valid
                if str(gpg.decrypt(str(transaction.signature))) != transaction.transactionString:
                    print("Transaction signature is not valid")
                    return False
        return True

    def newGetBalance(self, wallet: Wallet):
        balance = wallet.rewards
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender.name == wallet.name:
                    balance -= transaction.amount
                if transaction.reciever.name == wallet.name:
                    balance += transaction.amount
        return balance

    def GenesisBlock(self):
        tArray = [Transaction(godWallet(1), godWallet(0), 1)]
        genesis = Block(tArray, 0, 0)
        genesis.prev = "None"
        return genesis

class Block:
    def __init__(self, transactions, index, prev):
        self.nonce = 0
        self.transactions = transactions
        self.index = index
        self.time = time.ctime()
        self.prev = prev
        self.hash = self.calculateHash()

    def getTransactions(self):
        for transaction in self.transactions:
            print(transaction.transactionString)

    def calculateHash(self):
            hashTransactions = ''
            for transaction in self.transactions:
                if transaction: #Handle genesis block
                    hashTransactions += transaction.transactionString
                else:
                    return 0
            hashString = (f'{hashTransactions}{self.prev}{self.index}{self.nonce}{self.time}').encode()
            return hashlib.sha256(hashString).hexdigest()

    def mineBlock(self, difficulty):
        target = ''
        for i in range(difficulty):
            target += '0'
        while self.hash[0:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculateHash()

class Transaction:
    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.time = time.ctime()
        self.transactionString = f'{self.sender.name} to {self.reciever.name}: {self.amount} at {self.time}'
        self.signature = self.getSignature()

    def getSignature(self): #encrypts transaction data
        encrypted_data = gpg.encrypt(
        self.transactionString,
        self.reciever.key.fingerprint,
        sign=self.sender.key.fingerprint,
        passphrase=self.reciever.name)
        self.signature = encrypted_data
        return encrypted_data
