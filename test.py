from blockchain import *
from wallet import *

import gnupg
import os

from blockchain import *

gpg = gnupg.GPG(gnupghome='/opt/homebrew/Cellar/gnupg')
gpg.encoding = 'utf-8'

blockchain =  Blockchain()
blockchain.difficulty = 5

god = godWallet(100)
me = Wallet('me')
you = Wallet('you')

t = [Transaction(god, me, 10)]

for i in t:
    blockchain.addTransaction(i)
