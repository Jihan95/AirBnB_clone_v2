#!/usr/bin/python3
""" app module """
from flask import Flask, abort, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(error):
    """remove the current SQLAlchemy Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
