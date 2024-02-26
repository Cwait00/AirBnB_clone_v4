#!/usr/bin/python3
"""initializes the api"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if __name__ == "__init__":
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.amenities import *  # Add this line to import amenities view
    from api.v1.views.cities import *
    from api.v1.views.users import *
    from api.v1.views.places_reviews import *
    from api.v1.views.places import *
