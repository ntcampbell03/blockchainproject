from blockchain import *
from wallet import *

blockchain =  Blockchain()
blockchain.difficulty = 5

god = godWallet(100)
me = Wallet()
you = Wallet()
