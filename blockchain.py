from wallet import *
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = [Block([Transaction('', '', 0)], 0)]
        self.length = 1
        self.difficulty = 1
        self.newTransactions = []

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
        except(NameError):
            print('Wallet does not exist!')


    def addBlock(self):
        for transaction in self.newTransactions:
            transaction.sender.sent += transaction.amount
            transaction.reciever.recieved += transaction.amount
            transaction.sender.getBalance()
            transaction.sender.futureBalance = transaction.sender.balance
            transaction.reciever.getBalance()
            transaction.reciever.futureBalance = transaction.reciever.balance
        newBlock = Block(self.newTransactions, self.length - 1)
        newBlock.mineBlock(self.difficulty)
        self.length += 1
        self.chain.append(newBlock)
        self.newTransactions = []

class Block:
    def __init__(self, transactions, index):
        self.nonce = 0
        self.transactions = transactions
        self.index = index
        self.time = time.ctime()
        self.prev = ''
        self.hash = self.calculateHash()

    def getTransactions(self):
        for i in self.transactions:
            print(f'{self.transactions[0].sender} to {self.transactions[0].reciever}: {self.transactions[0].amount}')

    def calculateHash(self):
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
        self.transactionString = f'{self.sender} to {self.reciever}: {self.amount}'
