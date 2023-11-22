from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def home():
    return redirect(url_for('admin'))

@app.route("/admin")
def login():
    return render_template("admin.html")