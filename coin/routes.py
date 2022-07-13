from flask import Flask, redirect
from flask import render_template, flash
from flask import Flask, jsonify, request, render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from coin.forms import *
from flask_bcrypt import bcrypt
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #password hashing
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8');
        keyGen = blockchainObj.generateKeys();
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hashed_password, key = keyGen);
        db.session.add(user);
        db.session.commit();
        login_user(user);
        nextPage = request.args.get('next');
        flash(f'Account created for @{form.username.data}! You are now logged in as well.', 'success')
        return redirect(nextPage) if nextPage else redirect(url_for('home'));
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first();
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data);
            nextPage = request.args.get('next');
            flash(f'Welcome! You are now logged in', 'success');
            return redirect(nextPage) if nextPage else redirect(url_for('home'));
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger');
            #return redirect(url_for('login'))
    return render_template('login.html', form=form);

@app.route("/logout")
def logout():
    logout_user();
    return redirect(url_for('home'));
    return render_template('mine.html', blockchain=blockchainObj)

@app.route("/transactions", methods=['GET', 'POST'])
def transactions():
    return render_template('transaction.html', blockchain=blockchainObj)

@app.route("/transaction/", methods=['GET', 'POST'])
def transaction():
    blockchainObj.addTransaction(Transaction(godWallet(100), Wallet("me"), 5))
    return render_template('transaction.html', blockchain=blockchainObj)
