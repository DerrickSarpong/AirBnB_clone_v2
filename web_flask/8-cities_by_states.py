#!/usr/bin/python3
"""
Defines a Flask web api for AirBNB clone
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_app_context(exc):
    storage.close()


@app.get("/cities_by_states", strict_slashes=False)
def get_states_list():
    """Displays all cities in a state in an html page"""
    states = storage.all(State)
    states = sorted(states.values(), key=lambda val: val.name)
    sorted_states = {}
    for state in states:
        sorted_states[state] = sorted(state.cities, key=lambda val: val.name)
    return render_template("8-cities_by_states.html",
                           sorted_states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
