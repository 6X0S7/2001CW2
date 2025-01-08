from flask import Blueprint, request, render_template, jsonify
from database.database import add_user, get_users  # Assuming these functions exist in your database

manage_users_route = Blueprint('manage_users', __name__)

# Route to add a user
@manage_users_route.route('/add_user', methods=['POST'])
def add_user_route():
    data = request.get_json()
    user_name = data.get('user_name')

    if not user_name:
        return jsonify({"error": "User name is required"}), 400

    add_user(user_name)
    return jsonify({"message": "User added successfully"}), 201

# Route to get all users
@manage_users_route.route('/get_users', methods=['GET'])
def get_users_route():
    users = get_users()  # Fetch all users from the database
    return render_template('get_users.html', users=users)
