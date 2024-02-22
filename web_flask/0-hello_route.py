#!/usr/bin/python3
"""
Defines a Flask web app with a single route
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
