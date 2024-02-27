#!/usr/bin/python3
"""This module contains the Flask application for the API.

This Flask application serves as the backend for the API, providing various
endpoints for interacting with the application data. It includes routes for
managing resources such as users, items, and orders.

Usage:
    To run the application, execute this script directly:
        $ python3 app.py

Configuration:
    The application can be configured using the following environment variables:
        - HBNB_API_HOST: Host IP address (default: '0.0.0.0')
        - HBNB_API_PORT: Port number (default: 5000)

"""

import os
import sys  # Importing sys module
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown app context and close the database connection."""
    storage.close()

# Handler for 404 errors
@app.errorhandler(404)
def handle_not_found_error(e):
    """Handle 404 errors by returning a JSON-formatted response."""
    response = jsonify(error="Not found")
    response.status_code = 404
    return response

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
