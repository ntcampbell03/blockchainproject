from flask import Flask
from blockchain import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'i like boys';

blockchainObj = Blockchain()
blockchainObj.difficulty = 5

from coin import routes
