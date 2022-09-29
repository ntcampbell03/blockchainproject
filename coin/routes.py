from flask import Flask, redirect
from flask import render_template, flash
from flask import Flask, request, render_template, url_for, flash, redirect, session
from flask_login import login_user, current_user, logout_user, login_required
import jsonpickle
from coin.forms import *
from coin.models import *
from sqlalchemy.orm.attributes import flag_modified

import copy
from blockchainJson import *
from . import app, bcrypt, db
from coin import blockchainObj, distributorObj

from collections import Counter

import psycopg2

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', blockchain=blockchainObj)

@app.route('/blockchain/<idx>')
@app.route("/blockchain")
def blockchain(idx = 0):
    if current_user.is_authenticated:
        blockchainObj.updateChain(current_user.node)
    distributorObj.setUserCount(len(User.query.filter().all()))
    chain = []
    for blockObj in blockchainObj.chain:
        chain.append(blockObj.hash)
    selectedBlock = blockchainObj.getBlock(int(idx))
    lastUpdated = blockchainObj.getBlock(blockchainObj.length-1).time
    return render_template('blockchain.html', blockchain=blockchainObj, chain=chain, selectedBlock = selectedBlock, lastUpdated=lastUpdated)


@app.route("/mine", methods=['GET', 'POST'])
def mine():
    if current_user.is_authenticated:
        blockchainObj.updateChain(current_user.node)
    reward = blockchainObj.getReward()
    return render_template('mine.html', blockchain=blockchainObj, success=False, reward=reward)

@app.route("/mineblock/", methods=['GET', 'POST'])
def mineblock():
    distributorObj.syncChain()
    retrans = current_user.wallet.mineBlock(blockchainObj)
    flag_modified(current_user, "wallet")
    db.session.commit()
    distributorObj.syncChain(remove=retrans)
    return redirect(url_for('mine'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #password hashing
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #wallet creating
        newWallet = Wallet(form.username.data)
        user = User(username=form.username.data, password=hashed_password, wallet=newWallet, node=distributorObj.randomNode())
        db.session.add(user)
        db.session.commit()
        login_user(user)
        distributorObj.setUserCount(len(User.query.filter().all()))
        nextPage = request.args.get('next')
        flash(f'Account created for @{form.username.data}! You are now logged in as well.', 'success')
        return redirect(nextPage) if nextPage else redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    distributorObj.setUserCount(db.session.query(User).count())
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            nextPage = request.args.get('next')
            blockchainObj.updateChain(current_user.node)
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



@app.route("/wallet", methods=['GET', 'POST'])
def wallet():
    blockchainObj.updateChain(current_user.node)
    distributorObj.setUserCount(len(User.query.filter().all()))
    balance = blockchainObj.getBalance(current_user.wallet)
    form = TransactionForm()
    if form.validate_on_submit():
        if form.reciever.data == "testaccount":
            print("HI")
            blockchainObj.addTransaction(Transaction(Wallet("Test Account"), current_user.wallet, form.amount.data))
        else:
            try:
                reciever = User.query.filter(User.username == form.reciever.data).all()[0].wallet
                t = Transaction(current_user.wallet, reciever, form.amount.data)
                blockchainObj.addTransaction(t)
            except:
                print("INVALID RECIEVER")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('wallet.html', blockchain=blockchainObj, balance=balance, form=form, date=date)

@app.route("/node", methods=['GET', 'POST'])
def node():
    def zoomList(item):
        return item[0]
    if current_user.is_authenticated:
        blockchainObj.updateChain(current_user.node)
    distributorObj.setUserCount(len(User.query.filter().all()))
    nodes = User.query.with_entities(User.node).all()
    nodes = map(zoomList, nodes)
    nodesDict = dict(Counter(sorted(nodes)).items())

    chains = distributorObj.generateNodeList()
    return render_template('node.html', blockchain=blockchainObj, nodesDict=nodesDict, chains=chains, current_user=current_user)

@app.route("/changeNode/<node>")
def changeNode(node):
    if current_user.is_authenticated:
        current_user.node = node
        db.session.commit()
        blockchainObj.updateChain(current_user.node)
    return redirect(url_for('node'))


@app.route("/delete/<int:id>")
def delete(id):
    user_to_delete = User.query.get_or_404(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return render_template('node.html', blockchain=blockchainObj)

@app.context_processor
def inject_menu():
    return dict(current_user=current_user)

@app.route("/addcoins")
def addcoins():
    blockchainObj.addTransaction(Transaction(Wallet("Test Account"), current_user.wallet, 20))
    return redirect(url_for('mine'))

@app.get("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "light":
        session["theme"] = "dark"
    else:
        session["theme"] = "light"

    return redirect(request.args.get("current_page"))

@app.get("/sync")
def sync():
    distributorObj.syncChain()
    return redirect(request.referrer)