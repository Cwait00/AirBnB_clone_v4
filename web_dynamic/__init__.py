from flask import Flask

app = Flask(__name__)

# Import views/routes
from . import views
