#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /1-hbnb: Renders 1-hbnb.html template.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/1-hbnb", strict_slashes=False)
def hbnb():
    """Renders 1-hbnb.html template."""
    return render_template("1-hbnb.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
