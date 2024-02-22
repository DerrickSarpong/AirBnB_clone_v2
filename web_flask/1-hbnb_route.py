#!/usr/bin/python3
"""
Defines a Flask web app with two routes
"""
from flask import Flask

app = Flask(__name__)


@app.get("/", strict_slashes=False)
def index():
    """
    Root endpoint of Flask application

    Returns:
        (str) Hello HBNB!
    """
    return "Hello HBNB!"


@app.get("/hbnb", strict_slashes=False)
def get_hbnb():
    """
    hbnb endpoint of Flask application

    Returns:
        HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
