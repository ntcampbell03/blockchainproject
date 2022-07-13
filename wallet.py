import gnupg
import os
from blockchain import *

gpg = gnupg.GPG(gnupghome='/opt/homebrew/Cellar/gnupg')
# gpg = gnupg.GPG(gnupghome='/Users/noahcampbell/Desktop/CS/blockchainproject/env/lib/python3.10/site-packages')

gpg.encoding = 'utf-8'

class Wallet:
    def __init__(self, name):
        self.name = name
        self.sent = 0
        self.recieved = 0
        self.balance = self.getBalance()
        self.futureBalance = self.balance
        self.key = self.generateKeys()

    def generateKeys(self):
        input_data = gpg.gen_key_input(
            name_email='noahc@berkeley.edu',
            no_protection=True,
            key_type='RSA',
            key_length=1024)

        self.key = gpg.gen_key(input_data)
        return self.key

    def getBalance(self):
        self.balance = self.recieved - self.sent
        return self.balance


class godWallet:
    def __init__(self, balance):
        self.name = 'god'
        self.sent = 0
        self.recieved = 0
        self.balance = balance
        self.futureBalance = balance
        self.key = self.generateKeys()

    def generateKeys(self):
        input_data = gpg.gen_key_input(
            name_email='noahc@berkeley.edu',
            no_protection=True,
            key_type='RSA',
            key_length=1024)

        self.key = gpg.gen_key(input_data)
        return self.key

    def getBalance(self):
        pass
