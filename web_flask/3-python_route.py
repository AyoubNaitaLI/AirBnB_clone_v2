#!/usr/bin/python3
"""
This is the python_route module
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


@app.route("/c/<text>")
def c(text):
    """ This is the c route """
    f_text = ""
    for c in text:
        if c == "_":
            f_text += " "
        else:
            f_text += c
    return f"C {f_text}"


@app.route("/python", defaults={'text': "is cool"})
@app.route("/python/<text>")
def python(text):
    """ This is the python route """
    f_text = ""
    for c in text:
        if c == "_":
            f_text += " "
        else:
            f_text += c
    return f"Python {f_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
