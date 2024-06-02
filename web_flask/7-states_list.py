#!/usr/bin/python3
"""
start app module
"""
from flask import Flask, render_template
import models
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    lists all of the states
    """
    states = models.storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(error):
    """
    remove the current SQLAlchemy Session
    """
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
