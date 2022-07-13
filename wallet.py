import gnupg
import os
from blockchain import *

gpg = gnupg.GPG(gnupghome='/opt/homebrew/Cellar/gnupg')
# gpg = gnupg.GPG(gnupghome='/Users/noahcampbell/Desktop/CS/blockchainproject/env/lib/python3.10/site-packages')
# gpg = gnupg.GPG(gnupghome='/Users/nikhiljain/Desktop/blockchainproject/env/lib/python3.9/site-packages/')
# gpg = gnupg.GPG(gnupghome='/Users/rithwikbabu/Documents/appcode/blockchainproject/env/lib/python3.9/site-packages/')

gpg.encoding = 'utf-8'

class Wallet:
    def __init__(self, name):
        self.name = str(name)
        self.sent = 0
        self.recieved = 0
        self.rewards = 0
        self.balance = self.getBalance()
        self.futureBalance = self.balance
        self.input_data = gpg.gen_key_input(
            name_real='hello',
            no_protection=True,
            key_type='RSA',
            key_length=1024)
        self.key = gpg.gen_key(self.input_data)

    def generateKeys(self): #Generates GPG keys for encryption and signing of transaction data
        input_data = gpg.gen_key_input(
            name_real='hello',
            no_protection=True,
            key_type='RSA',
            key_length=1024)
        self.key = gpg.gen_key(input_data)
        return self.key

    def getBalance(self):
        self.balance = self.recieved - self.sent + self.rewards
        return self.balance
    
    def mineBlock(self, Blockchain):
        self.rewards = Blockchain.addBlock()
        self.balance = self.getBalance()

    




class godWallet:
    def __init__(self, balance):
        self.name = 'god'
        self.sent = 0
        self.recieved = 0
        self.balance = balance
        self.futureBalance = balance
        self.key = self.generateKeys()

    def generateKeys(self):
        return gpg.gen_key(gpg.gen_key_input(name_real = 'noah', no_protection = True, key_type = 'RSA', key_length = 1024))

    def getBalance(self):
        pass
