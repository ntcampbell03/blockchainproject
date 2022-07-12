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
    chain = []
    for blockObj in blockchainObj.chain:
        chain.append(blockObj.hash)
    return render_template('blockchain.html', blockchain=blockchainObj, chain=chain)


@app.route("/mine", methods=['GET', 'POST'])
def mine():
    return render_template('mine.html')

@app.route("/mineblock/", methods=['GET', 'POST'])
def mineblock():
    blockchainObj.addBlock()
    return render_template('mine.html')