from flask import Blueprint, request, jsonify
from database.database import add_trail  # Assuming this is the function to add a trail

manage_trail_route = Blueprint('manage_trail', __name__)

# Route to add a trail
@manage_trail_route.route('/add_trail', methods=['POST'])
def add_trail_route_func():
    data = request.get_json()
    trail_name = data.get('trail_name')
    trail_length = data.get('trail_length')

    if not trail_name or not trail_length:
        return jsonify({"error": "Trail name and length are required"}), 400

    add_trail(trail_name, trail_length)
    return jsonify({"message": "Trail added successfully"}), 201

