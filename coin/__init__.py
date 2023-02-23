from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blockchainJson import *
from nodedistributor import *
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'i like boys'
url = os.environ["CRUNCHY_DATABASE_URL"]
# url = "postgres://postgres:UlWFrxixw9haCj7lZ49NrGzXdfLTE5HDi24ru634wPW0vy3d1fz1BRTQJJT48dHV@p.oyoqg2imozh7jop7q7pgve43yq.db.postgresbridge.com:5432/postgres"
url = url[:8] + "ql" + url[8:]

app.config['SQLALCHEMY_DATABASE_URI'] = url
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
