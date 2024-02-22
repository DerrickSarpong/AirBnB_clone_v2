#!/usr/bin/python3
"""
Defines a Flask web app with routes
"""
from flask import Flask
from flask import render_template

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


@app.get("/c/<text>", strict_slashes=False)
def get_c(text):
    """
    Returns C followed by the path parameter
    """
    return f"C {text}".replace("_", " ")


@app.get("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.get("/python/<text>", strict_slashes=False)
def get_python(text):
    """
    Returns Python followed by the path parameter
    """
    return f"Python {text}".replace("_", " ")


@app.get("/number/<int:n>", strict_slashes=False)
def get_number(n):
    """
    Returns 'n is a number if the route param is an int
    """

    return f"{n} is a number"


@app.get("/number_template/<int:n>", strict_slashes=False)
def get_number_template(n):
    """
    Displays input number in an html page
    """
    return render_template("5-number.html", n=n)


@app.get("/number_odd_or_even/<int:n>", strict_slashes=False)
def get_number_odd_or_even(n):
    """
    Displays input number in an html page
    and indicates if it is even or odd
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
