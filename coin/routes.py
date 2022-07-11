from flask import Flask
from flask import render_template
from datetime import datetime
from . import app

@app.route("/")
@app.route("/<name>")
def home(name = None):
    return render_template('home.html', name=name, date=datetime.now());
