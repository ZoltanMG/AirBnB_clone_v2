#!/usr/bin/python3
"""
Flask app with airbnb clone
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def cities_by_states():
    """
    route /states_list that send the states to jinja2
    """
    states = storage.all("State")

    return render_template("7-states_list.html", states=states)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    sohw only cities of estates of id
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", states=state)

    return render_template("9-states.html")

@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    """
    teardown_appcontext to close session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
