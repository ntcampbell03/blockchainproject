import json
from blockchainJson import *

import gnupg
import os

blockchain1 =  Blockchain()
blockchain1.writeChain()
print(blockchain1.chain)


