from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "test1"

@app.route("/hello")
def index():
    flash("This is a flash message!")
    return render_template("index.html")