from flask import Flask, redirect
from flask import render_template, flash
from datetime import datetime

from blockchain import Transaction
from . import app
from coin import blockchainObj, Wallet, godWallet


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
    return render_template('mine.html', blockchain=blockchainObj)

@app.route("/mineblock/", methods=['GET', 'POST'])
def mineblock():
    blockchainObj.addBlock()
    return render_template('mine.html', blockchain=blockchainObj)

@app.route("/transactions", methods=['GET', 'POST'])
def transactions():
    return render_template('transaction.html', blockchain=blockchainObj)

@app.route("/transaction/", methods=['GET', 'POST'])
def transaction():
    blockchainObj.addTransaction(Transaction(godWallet(100), Wallet("me"), 5))
    return render_template('transaction.html', blockchain=blockchainObj)

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')