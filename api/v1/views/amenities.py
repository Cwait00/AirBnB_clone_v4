#!/usr/bin/python3

from flask import Flask, jsonify, request, abort
from models import storage
from models.amenity import Amenity

# Import app and CORS here if needed

# Define your Flask Blueprint
# amenities_bp = Blueprint('amenities', __name__)

# Define your route functions
# Example:
# @amenities_bp.route('/api/v1/amenities', methods=['GET'])
def get_all_amenities():
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])

# Implement other route functions for GET, POST, PUT, DELETE as described

# Example:
# @amenities_bp.route('/api/v1/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    else:
        abort(404)

# Implement other route functions for GET, POST, PUT, DELETE as described

# Example:
# @amenities_bp.route('/api/v1/amenities', methods=['POST'])
def create_amenity():
    if not request.json:
        abort(400, 'Not a JSON')
    if 'name' not in request.json:
        abort(400, 'Missing name')
    data = request.json
    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201

# Implement other route functions for GET, POST, PUT, DELETE as described
