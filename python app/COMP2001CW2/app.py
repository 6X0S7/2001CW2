from flask import Flask
from routes.manage_users import manage_users_route  # Change to import from the new file
from routes.manage_trails import manage_trail_route  # Change to import from the new file
import requests

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(manage_users_route)
app.register_blueprint(manage_trail_route)

# API endpoint for authentication
auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'

# Function to authenticate the user
def authenticate_user():
    # Get credentials from the user
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Create a dictionary for credentials
    credentials = {
        'email': email,
        'password': password
    }

    # Send POST request for authentication
    response = requests.post(auth_url, json=credentials)

    # Handle the response
    if response.status_code == 200:
        try:
            # Parse the JSON response
            json_response = response.json()
            
            # Check if the response contains ["Verified", "True"]
            if len(json_response) > 1 and json_response[0] == "Verified" and json_response[1] == "True":
                print("Authenticated successfully.")
                return True
            else:
                print("Authentication failed: User not verified.")
                return False
        
        except requests.JSONDecodeError:
            print("Response is not valid JSON. Raw response content:")
            print(response.text)
            return False
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print("Response content:", response.text)
        return False

# Check authentication before running the app
if authenticate_user():
    app.run(debug=True)
else:
    print("Authentication failed. Flask server will not start.")
