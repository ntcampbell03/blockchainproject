from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blockchainJson import *
from nodedistributor import *
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'i like boys'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xpahdelqnuopvl:edcc7b324dd36ca1f59a3849bf503c52e1e3499cd64835f88ad7f96401d3d31c@ec2-100-26-39-41.compute-1.amazonaws.com:5432/d8lbeqdtcsvnma'
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
