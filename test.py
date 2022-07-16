from blockchain import *

import gnupg
import os

blockchain =  Blockchain()

god = godWallet('god')
me = Wallet('me')
you = Wallet('you')

t = Transaction(god, me, 10)
u = Transaction(me, you, 5)


blockchain.addTransaction(t)
blockchain.addTransaction(u)
blockchain.addBlock()

print(blockchain.getBalance(me))



