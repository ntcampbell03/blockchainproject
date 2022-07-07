from blockchain import *

class Wallet:
    def __init__(self):
        self.sent = 0
        self.recieved = 0
        self.balance = self.getBalance()
        self.futureBalance = self.balance

    def generateKeys():
        pass

    def getBalance(self):
        self.balance = self.recieved - self.sent
        return self.balance

class godWallet:
    def __init__(self, balance):
        self.sent = 0
        self.recieved = 0
        self.balance = balance
        self.futureBalance = balance

    def getBalance(self):
        pass
