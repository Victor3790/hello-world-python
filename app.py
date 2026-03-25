from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "test1"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")
def hello():
    flash("This is a flash message!")
    return render_template("hello.html", subtitle="Welcome to the Hello Page")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if username == "admin" and password == "password":
        return render_template("welcome.html", username=username)
    else:
        flash("Invalid credentials. Please try again.")
        return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)