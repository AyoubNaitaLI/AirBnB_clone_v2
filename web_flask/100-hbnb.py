#!/usr/bin/python3
"""
This is the hbnb module
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ closing the storage """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """hbnb filter"""
    states = storage.all(State).values()
    states_srtd = sorted(states, key=lambda obj: obj.name)
    amnt = storage.all(Amenity).values()
    amnt_srtd = sorted(amnt, key=lambda obj: obj.name)
    plc = storage.all(Place).values()
    plc_srtd = sorted(plc, key=lambda obj: obj.name)
    return render_template("100-hbnb.html", amnt=amnt_srtd,
                           states=states_srtd, places=plc_srtd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
