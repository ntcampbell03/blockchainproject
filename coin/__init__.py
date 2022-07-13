from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blockchain import *
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'i like boys';

blockchainObj = Blockchain()
blockchainObj.difficulty = 5

loginManager = LoginManager(app);
loginManager.login_view = 'login';
loginManager.login_message_category = 'info';

db = SQLAlchemy(app);
bcrypt = Bcrypt(app);

from coin import routes
