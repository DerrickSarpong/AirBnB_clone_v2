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


@app.get("/states", strict_slashes=False, defaults={"id": None})
@app.get("/states/<id>", strict_slashes=False)
def get_states(id):
    """Displays states in an html page"""
    if id is not None:
        states = storage.all(State)
        state = None
        cities = None
        for s in states.values():
            if s.id == id:
                state = s
                cities = sorted(state.cities, key=lambda val: val.name)
        return render_template("9-states.html",
                               state=state, cities=cities, id=id)
    else:
        states = storage.all(State)
        states = sorted(states.values(), key=lambda val: val.name)
        return render_template("9-states.html", states=states, id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
