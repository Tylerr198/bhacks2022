from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page! </h1>"

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")
    
app.route("/<user>")
def user(usr):
    return f"wassup {usr}"

if __name__ == "__main__":
    app.run()
    
    
    