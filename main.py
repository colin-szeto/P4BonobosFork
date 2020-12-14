from datetime import datetime
from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/database")
def database():
    return render_template("database.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")