from wallet import *
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = [Block(None, 0)]
        self.length = 1
        self.difficulty = 1
        self.newTransactions = []
        self.miningReward = 10

    def getBlock(self, n):
        return self.chain[n]

    def getLastBlock(self):
        return self.chain[-1]

    def addTransaction(self, transaction):
        try:
            if transaction.sender.futureBalance >= transaction.amount:
                self.newTransactions.append(transaction)
                transaction.sender.futureBalance -= transaction.amount
            else:
                print('Wallet has insufficient balance!')
        except NameError:
            print('Wallet does not exist!') #Try except doesnt work


    def addBlock(self):
        if self.newTransactions:
            for transaction in self.newTransactions:
                if str(gpg.decrypt(str(transaction.signature), passphrase = transaction.reciever.name)) == transaction.transactionString:
                    transaction.sender.sent += transaction.amount
                    transaction.reciever.recieved += transaction.amount
                    transaction.sender.getBalance()
                    transaction.sender.futureBalance = transaction.sender.balance
                    transaction.reciever.getBalance()
                    transaction.reciever.futureBalance = transaction.reciever.balance
            newBlock = Block(self.newTransactions, self.length)
            newBlock.mineBlock(self.difficulty)
            if self.getLastBlock().index <= newBlock.index:
                self.length += 1
                self.chain.append(newBlock)
                self.newTransactions = []
        else:
            print("No pending transactions")

class Block:
    def __init__(self, transactions, index):
        self.nonce = 0
        self.transactions = transactions
        self.index = index
        self.time = time.ctime()
        self.prev = ''
        self.hash = self.calculateHash()

    def getPendingTransactions(self):
        for transaction in self.transactions:
            print(f'{transaction.sender.name} to {transaction.reciever.name}: {transaction.amount}')

    def calculateHash(self):
        if not self.transactions: #deal with genesis block
            return 0
        else:
            hashTransactions = ''
            for transaction in self.transactions:
                hashTransactions += transaction.transactionString
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

    def getSignature(self):
        encrypted_data = gpg.encrypt(
        self.transactionString,
        self.reciever.key.fingerprint,
        sign=self.sender.key.fingerprint,
        passphrase = self.reciever.name)
        self.signature = encrypted_data
        return encrypted_data
