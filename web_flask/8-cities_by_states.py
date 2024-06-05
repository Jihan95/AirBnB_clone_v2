#!/usr/bin/python3
""" App module """
from flask import Flask, render_template
import models
from models.state import State


app = Flask(__name__)

def main():
    """ main function """
    @app.route('/states_list', strict_slashes=False)
    def list_states():
        """ view that lists all of the states """
        states = storage.all(State).values()
        return render_template('7-states_list.html', states=states)


    @app.route('/cities_by_states', strict_slashes=False)
    def list_state_cities():
        """ view that lists all cities by their states """
        states = models.storage.all(State).values()
        return render_template('8-cities_by_states.html', states=states)


    @app.teardown_appcontext
    def close(error):
        """ remove the current SQLAlchemy Session """
        models.storage.close()


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=5000)
