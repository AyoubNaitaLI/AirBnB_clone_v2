#!/usr/bin/python3
"""
This is the cities_by_state_template module
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ closing the storage """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """ Listing the cities by state """
    states = storage.all(State).values()
    states_A_Z = sorted(list(states), key=lambda att: att.name)
    print(states_A_Z)
    return render_template("8-cities_by_states.html", states=states_A_Z)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
