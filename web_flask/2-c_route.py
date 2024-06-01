#!/usr/bin/python3
""" app module """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ hello hbnb """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ c is fun """
    return f"c {text.replace('_', ' ')}"


@app.errorhandler(404)
def page_not_found(e):
    """ Custom 404 error page """
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
