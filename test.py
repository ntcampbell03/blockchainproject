from blockchain import *

import gnupg
import os

blockchain =  Blockchain()

god = godWallet('god')
me = Wallet('me')
you = Wallet('you')

t = Transaction(god, me, 10)
u = Transaction(me, you, 5)
v = Transaction(you, me, 5)

blockchain.addTransaction(t)
blockchain.addBlock()



