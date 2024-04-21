#!/usr/bin/python3
"""
This is the hbnb_route module
"""


from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ My first route """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ My 2nd route """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
