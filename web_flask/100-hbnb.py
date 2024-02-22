#!/usr/bin/python3
"""
Defines a Flask web api for AirBNB clone
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def close_app_context(exc):
    storage.close()


@app.get("/hbnb", strict_slashes=False)
def get_hbnb():
    """Displays hbnb main page"""
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    sorted_states = {}
    for state in states:
        sorted_states[state] = sorted(state.cities, key=lambda city: city.name)

    amenities = storage.all(Amenity)
    amenities = sorted(amenities.values(), key=lambda amenity: amenity.name)

    places = storage.all(Place)
    places = sorted(places.values(), key=lambda place: place.name)
    places_users = {}
    users = storage.all(User).values()

    for place in places:
        places_users[place] = next(
            (user for user in users if user.id == place.user_id), None)

    return render_template("100-hbnb.html",
                           states=sorted_states,
                           amenities=amenities,
                           places=places_users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
