from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blockchainJson import *
from nodedistributor import *
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'i like boys'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

blockchainObj = Blockchain(True)
distributorObj = NodeDistributor()
# blockchainObj.difficulty = 5

loginManager = LoginManager(app)
loginManager.login_view = 'login'
loginManager.login_message_category = 'info'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from coin import routes
