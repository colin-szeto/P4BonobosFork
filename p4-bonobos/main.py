from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
import data

@app.route("/landing")
@app.route("/")
def landing2():
    return render_template("landing.html")

@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5001")