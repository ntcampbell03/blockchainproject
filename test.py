from blockchain import *
from wallet import *

import gnupg
import os

from blockchain import *

blockchain =  Blockchain()

god = godWallet(100)
me = Wallet('me')
you = Wallet('you')

t = Transaction(god, me, 10)
blockchain.addTransaction(t)
blockchain.addBlock()

print(me.balance)


