#!/usr/bin/python3

from flask import Flask
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

if __name__ == "__main__":
    # Get host and port from environment variables, default to 0.0.0.0:5000
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
