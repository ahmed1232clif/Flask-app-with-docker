from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return redirect(url_for('admin'))

@app.route("/admin")
def admin():
    return render_template("admin.html")
