from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blockchain import *
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'i like boys'
url = os.environ["DATABASE_URL"]
# url = "postgres://nlydgbgfxpamym:b4c2d2f8e38a021ceb0d5b733a473d237ed0c9dbb28f0d2c685c3ce8b1f8de92@ec2-54-86-106-48.compute-1.amazonaws.com:5432/dcq1sg4ngoqh2m"
url = url[:8] + "ql" + url[8:]

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

blockchainObj = Blockchain()
# blockchainObj.difficulty = 5

loginManager = LoginManager(app)
loginManager.login_view = 'login'
loginManager.login_message_category = 'info'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from coin import routes
