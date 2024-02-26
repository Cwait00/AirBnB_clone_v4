#!/usr/bin/python3

import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

# Create Flask app instance
app = Flask(__name__)

# Register blueprint
app.register_blueprint(app_views, url_prefix="/api/v1")

# Teardown method to close database connection
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

# Handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    # Get host and port from environment variables, default to 0.0.0.0:5000
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
