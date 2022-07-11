from flask import Flask
app = Flask(__name__)

from coin import routes
