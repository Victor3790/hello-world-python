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

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if username == "admin" and password == "password":
        flash("Login successful!")
        return render_template("hello.html")
    else:
        flash("Invalid credentials. Please try again.")
        return render_template("login.html")