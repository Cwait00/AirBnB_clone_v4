#!/usr/bin/python3

from flask import Blueprint

# Create Blueprint instance for API version 1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import of all views in the package
from api.v1.views.index import *
