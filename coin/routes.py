from flask import Flask
from flask import render_template
from datetime import datetime
from . import app
from coin import blockchainObj


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', blockchain=blockchainObj)


@app.route("/blockchain")
def blockchain():
    return render_template('blockchain.html', blockchain=blockchainObj)


@app.route("/mine")
def mine():
    return render_template('mine.html')
