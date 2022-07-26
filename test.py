from blockchain import *

import gnupg
import os

blockchain1 =  Blockchain()
blockchain1.difficulty = 5

god = godWallet('god')
me = Wallet('me')
you = Wallet('you')

t = Transaction(god, me, 10)
u = Transaction(me, you, 5)


blockchain1.addTransaction(t)
blockchain1.addTransaction(u)
blockchain1.addBlock()

print(blockchain1.chain)


