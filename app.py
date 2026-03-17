from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "test1"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")
def hello():
    flash("This is a flash message!")
    return render_template("hello.html")

@app.route("/login")
def login():
    return render_template("login.html")