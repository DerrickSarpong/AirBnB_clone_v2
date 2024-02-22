#!/usr/bin/python3
"""
Defines a Flask web api for AirBNB clone
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close_app_context(exc):
    storage.close()


@app.get("/hbnb_filters", strict_slashes=False)
def get_hbnb_filters():
    """Displays hbnb filters in an html page"""
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    sorted_states = {}
    for state in states:
        sorted_states[state] = sorted(state.cities, key=lambda city: city.name)

    amenities = storage.all(Amenity)
    amenities = sorted(amenities.values(), key=lambda amenity: amenity.name)

    return render_template("10-hbnb_filters.html",
                           states=sorted_states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
