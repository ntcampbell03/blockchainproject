from flask import Flask, redirect
from flask import render_template, flash
from flask import Flask, jsonify, request, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from coin.forms import *
from coin.models import *
from sqlalchemy.orm.attributes import flag_modified

import copy
from blockchain import *
from . import app, bcrypt, db
from coin import blockchainObj

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', blockchain=blockchainObj)

@app.route('/blockchain/<idx>')
@app.route("/blockchain")
def blockchain(idx = 0):
    chain = []
    for blockObj in blockchainObj.chain:
        chain.append(blockObj.hash)
    selectedBlock = blockchainObj.getBlock(int(idx))
    lastUpdated = blockchainObj.getBlock(blockchainObj.length-1).time
    return render_template('blockchain.html', blockchain=blockchainObj, chain=chain, selectedBlock = selectedBlock, lastUpdated=lastUpdated)


@app.route("/mine", methods=['GET', 'POST'])
def mine():
    return render_template('mine.html', blockchain=blockchainObj, success=False)

@app.route("/mineblock/", methods=['GET', 'POST'])
def mineblock():
    current_user.wallet.mineBlock(blockchainObj)
    flag_modified(current_user, "wallet")
    db.session.commit()
    return render_template('mine.html', blockchain=blockchainObj, success=True)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #password hashing
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #wallet creating
        newWallet = Wallet(form.username.data)
        user = User(username=form.username.data, password=hashed_password, wallet=newWallet)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        nextPage = request.args.get('next')
        flash(f'Account created for @{form.username.data}! You are now logged in as well.', 'success')
        return redirect(nextPage) if nextPage else redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            nextPage = request.args.get('next')
            return redirect(nextPage) if nextPage else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            #return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
    # return render_template('mine.html', blockchain=blockchainObj)

@app.route("/transactions", methods=['GET', 'POST'])
def transactions():
    form = TransactionForm()
    if form.validate_on_submit():
        reciever = User.query.filter(User.username == form.reciever.data).all()[0].wallet
        t = Transaction(current_user.wallet, reciever, form.amount.data)
        blockchainObj.addTransaction(t)
    return render_template('transaction.html', blockchain=blockchainObj, form=form)

@app.route("/transaction/", methods=['GET', 'POST'])
def transaction():
    form = TransactionForm()
    blockchainObj.addTransaction(Transaction(godWallet("hi"), current_user.wallet, 5))
    
    return render_template('wallet.html', blockchain=blockchainObj, form=form)

@app.route("/wallet", methods=['GET', 'POST'])
def wallet():
    balance = blockchainObj.getBalance(current_user.wallet)
    form = TransactionForm()
    if form.validate_on_submit():
        reciever = User.query.filter(User.username == form.reciever.data).all()[0].wallet
        t = Transaction(current_user.wallet, reciever, form.amount.data)
        blockchainObj.addTransaction(t)
    return render_template('wallet.html', wallet=current_user.wallet, blockchain=blockchainObj, balance=balance, form=form)