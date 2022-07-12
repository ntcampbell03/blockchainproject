from flask import Flask
from blockchain import *

app = Flask(__name__)

blockchainObj = Blockchain()
blockchainObj.difficulty = 5

from coin import routes
