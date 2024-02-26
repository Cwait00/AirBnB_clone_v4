#!/usr/bin/python3
"""This module contains the Flask application for the API."""

import os
import sys
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
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
