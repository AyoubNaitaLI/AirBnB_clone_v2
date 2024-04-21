#!/usr/bin/python3
"""
This is the states module
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ closing the storage """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ Listing the state """
    states = storage.all(State).values()
    states_A_Z = sorted(list(states), key=lambda att: att.name)
    return render_template("7-states_list.html", states=states_A_Z)


@app.route("/states/<id>", strict_slashes=False)
def state_by_id(id):
    """ search state by id """
    st = None
    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            st = state
    return render_template("9-states.html", state=st)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
