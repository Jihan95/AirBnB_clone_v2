#!/usr/bin/python3
""" app module """
from flask import Flask, abort

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
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Python is cool """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer """
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    """ Custom 404 error page """
    return (
            '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n'''
            '''<title>404 Not Found</title>\n'''
            '''<h1>Not Found</h1>\n'''
            '''<p>The requested URL was not found on the server. '''
            '''If you entered the URL manually please check your spelling '''
            '''and try again.</p>\n''', 404
            )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
