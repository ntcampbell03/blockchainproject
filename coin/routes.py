from flask import Flask
from flask import render_template
from datetime import datetime
from . import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', date=datetime.now());
