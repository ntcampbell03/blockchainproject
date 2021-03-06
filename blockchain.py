# import hashlib
# import time
# import math
# import gnupg

# gpg = gnupg.GPG()
# # gpg = gnupg.GPG(gnupghome='/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages')
# # gpg = gnupg.GPG(gnupghome='/Users/nikhiljain/Desktop/blockchainproject/env/lib/python3.9/site-packages/')
# # gpg = gnupg.GPG(gnupghome='/Users/rithwikbabu/Documents/appcode/blockchainproject/env/lib/python3.9/site-packages/')

# gpg.encoding = 'utf-8'


# class Blockchain:
#     def __init__(self):
#         self.chain = [self.GenesisBlock()]
#         self.length = 1
#         self.difficulty = 0
#         self.newTransactions = []
#         self.numTransactions = 0
#         self.miningReward = 0

#     def getBlock(self, n):
#         return self.chain[n]

#     def getLastBlock(self):
#         return self.chain[-1]

#     # Iterates through all confirmed blocks to determine the balance of a wallet
#     def getBalance(self, wallet):
#         if isinstance(wallet, godWallet):
#             return float('inf')  # Infinite
#         balance = 0
#         for block in self.chain:
#             for transaction in block.transactions:
#                 if transaction.sender.name == wallet.name:
#                     balance -= transaction.amount
#                 if transaction.reciever.name == wallet.name:
#                     balance += transaction.amount
#         return balance

#     def getPendingBalance(self, wallet):  # Also iterates through pending transactions
#         if isinstance(wallet, godWallet):
#             return float('inf')  # Infinite
#         balance = 0
#         for block in self.chain:
#             for transaction in block.transactions:
#                 if transaction.sender.name == wallet.name:
#                     balance -= transaction.amount
#                 if transaction.reciever.name == wallet.name:
#                     balance += transaction.amount
#         for transaction in self.newTransactions:
#             if transaction.sender.name == wallet.name:
#                 balance -= transaction.amount
#             if transaction.reciever.name == wallet.name:
#                 balance += transaction.amount
#         return balance

#     # Adds a transaction to self.newTransactions
#     def addTransaction(self, newTransaction):
#         try:
#             senderCurBalance = self.getPendingBalance(newTransaction.sender)
#             receiverCurBalance = self.getPendingBalance(
#                 newTransaction.reciever)
#             if senderCurBalance >= newTransaction.amount:  # Checks if balance is sufficient
#                 self.newTransactions.append(newTransaction)
#                 self.numTransactions += 1
#                 self.miningReward = int(
#                     10 * math.log(.2 * self.numTransactions + 1) ** (1.2))
#             else:
#                 print('Wallet has insufficient balance!')
#         except NameError:
#             # Tryblockchain.addTransaction(t) except doesnt work
#             print('Wallet does not exist!')

#     def addBlock(self):  # Adds a block to the blockchain
#         if self.newTransactions:
#             for transaction in self.newTransactions:
#                 if not gpg.verify(transaction.signature):
#                     raise ValueError(
#                         "Transaction signature could not be verified")
#             if self.numTransactions > 10:  # Adjusts the difficulty based on the number of transactions
#                 newBlock = Block(self.newTransactions, self.length, self.getLastBlock(
#                 ).hash, self.difficulty - 1 if self.difficulty - 1 >= 0 else 0)
#             elif self.numTransactions > 25:
#                 newBlock = Block(self.newTransactions, self.length, self.getLastBlock(
#                 ).hash, self.difficulty - 2 if self.difficulty - 2 >= 0 else 0)
#             else:
#                 newBlock = Block(self.newTransactions, self.length,
#                                  self.getLastBlock().hash, self.difficulty)
#             newBlock.mineBlock(newBlock.curDifficulty)
#             if self.getLastBlock().index <= newBlock.index:
#                 self.chain.append(newBlock)
#                 self.length += 1
#                 self.newTransactions = []
#                 self.numTransactions = 0

#                 return self.miningReward
#                 # if self.numTransactions > 10: # Increases rewards for more transactions in a block
#                 #     self.numTransactions = 0
#                 #     return self.miningReward + 5
#                 # elif self.numTransactions > 25:
#                 #     self.numTransactions = 0
#                 #     return self.miningReward + 10
#                 # elif self.numTransactions > 100:
#                 #     self.numTransactions = 0
#                 #     return self.miningReward + 25
#                 # else:
#                 #     self.numTransactions = 0
#                 #     return self.miningReward
#         else:
#             print("No pending transactions")
#             return 0

#     # Verifies hashes of the blocks and the signatures of the transactions
#     def verifyBlockchain(self):
#         prevHash = '0'
#         for i, curBlock in enumerate(self.chain[1:]):
#             if curBlock.hash != curBlock.calculateHash():  # Check if hash is legitimate
#                 print("Hash does not match data")
#                 return False
#             # Check if hash is acceptable
#             for char in curBlock.hash[0:curBlock.curDifficulty]:
#                 if char != '0':
#                     print("Hash does not meet requirements")
#                     return False
#             if curBlock.prev != prevHash:  # Check if prev is acceptable
#                 print("Previous hash does not match", i)
#                 return False
#             prevHash = curBlock.hash
#             for transaction in curBlock.transactions:  # Check if transaction signatures are valid
#                 rewardTransactions = 0
#                 if not gpg.verify(transaction.signature):
#                     print("Transaction signature is not valid")
#                     return False
#                 # if isinstance(transaction.sender, godWallet): # Checks to see how many reward transactions there are
#                 #     rewardTransactions += 1
#                 #     if rewardTransactions > 1:
#                 #         print("Too many reward transactions")
#                 #         return False
#         return True

#     def GenesisBlock(self):  # Creates genesis block
#         genesis = Block(
#             [Transaction(godWallet("1"), godWallet("2"), 0)], 0, "None", 0)
#         return genesis


# class Wallet:
#     def __init__(self, name):
#         self.name = str(name)
#         self.input_data = gpg.gen_key_input(
#             name_real=self.name,
#             no_protection=True,
#             key_type='RSA',
#             key_length=1024)
#         self.key = gpg.gen_key(self.input_data)

#     # Mines a block and adds a reward transaction to the pending transactions
#     def mineBlock(self, Blockchain):
#         print("ur trolling")
#         reward = Blockchain.addBlock()
#         rewardTransaction = Transaction(godWallet(1), self, reward)
#         Blockchain.addTransaction(rewardTransaction)


# class godWallet(Wallet):  # Wallet with infinite balance
#     pass


# class Block:
#     def __init__(self, transactions, index, prev, curDifficulty):
#         self.nonce = 0
#         self.transactions = transactions
#         self.index = index
#         self.time = time.ctime()
#         self.prev = prev
#         self.hash = self.calculateHash()
#         self.curDifficulty = curDifficulty

#     def getTransactions(self):
#         for transaction in self.transactions:
#             print(transaction.transactionString)

#     def calculateHash(self):
#         hashTransactions = ''
#         if self.prev != "None":  # Handle genesis block
#             for transaction in self.transactions:
#                 hashTransactions += transaction.transactionString
#         else:
#             return '0'
#         hashString = (
#             f'{hashTransactions}{self.prev}{self.index}{self.nonce}{self.time}').encode()
#         return hashlib.sha256(hashString).hexdigest()

#     def mineBlock(self, difficulty):
#         target = ''
#         for i in range(difficulty):
#             target += '0'
#         while self.hash[0:difficulty] != target:
#             self.nonce += 1
#             self.hash = self.calculateHash()
#             time.sleep(0.5)  # Slows down mining


# class Transaction:
#     def __init__(self, sender, reciever, amount):
#         self.sender = sender
#         self.reciever = reciever
#         self.amount = amount
#         self.time = time.ctime()
#         self.transactionString = f'{self.sender.name} to {self.reciever.name}: {self.amount} at {self.time}'
#         self.signature = self.getSignature()

#     def getSignature(self):  # Signs transaction data
#         signed_data = str(gpg.sign(self.transactionString,
#                           keyid=self.sender.key.fingerprint))
#         self.signature = signed_data
#         return signed_data
