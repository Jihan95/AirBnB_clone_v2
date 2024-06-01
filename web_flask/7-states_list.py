#!/usr/bin/python3
"""
Starts a Flask web application that lists State objects from the database.

This application connects to a storage system, retrieves State objects,
and displays them on a web page sorted by name. It also ensures that the
SQLAlchemy session is properly closed after each request.

Routes:
    /states_list: Displays a list of all State objects.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Lists all State objects present in DBStorage sorted by name (A->Z).

    Retrieves all State objects from the storage, sorts them by their
    name attribute, and renders them using the '7-states_list.html' template.

    Returns:
        str: The rendered HTML template displaying the list of states.
    """
    states_dict = storage.all(State)
    states = list(states_dict.values())
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close(e):
    """
    Remove the current SQLAlchemy Session.

    This function is called automatically after each request to ensure that
    the SQLAlchemy session is properly closed, preventing potential database
    connection issues.

    Args:
        e (Exception): An exception that occurred (if any).

    Returns:
        None
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
