#!/usr/bin/python3
"""
script that starts a Flask web application:
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    route /
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    route /hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    route /c with text variable
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """
    route /python with default variable text = "is cool"
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    route /number only integers
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    route /number_template only integers
    """
    return render_template("5-number.html", n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
