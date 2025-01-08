**Database used is the exact copy submitted in CW1 report.**
**CW1 report has detailed overview and code used.**
**There is also a docker file attached to this GitHub repo. Use it if you can.**

📚 Detailed Overview
Core Features
Authentication

Verifies users against an external API.
Requires valid credentials (email and password).
Ensures only authenticated users can start the server.
User Management

Add a user to the users table in the database.
Retrieve a list of all users for display or further processing.
Trail Management

Add trail details such as name and length to the trails table.
Database Operations

Uses pyodbc to connect to an SQL Server database.
Modular database functions for easy maintenance and scalability.
Blueprint Architecture

Routes for users and trails are organized using Flask blueprints.
🛠 How the Program Works
Authentication
When the program starts, it prompts for user credentials (email and password).
These credentials are sent to the authentication API:

python
Copy code
auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'
response = requests.post(auth_url, json=credentials)
If the response confirms verification, the server starts.
Otherwise, the program exits, preventing unauthorized access.
Database Connection
The pyodbc library handles connections to a local SQL Server database:

python
Copy code
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=COMP2001_CW2;"
    "UID=SA;"
    "PWD=C0mp2001!;"
)
User and Trail Management

Add User: Users are added via a POST request to /add_user.

Example: { "user_name": "John Doe" }
Inserts data into the users table using:
sql
Copy code
INSERT INTO [CW2].[users] (user_name) VALUES (?)
Get Users: A GET request to /get_users fetches all users.

The users are returned and displayed in an HTML table using a template.
Add Trail: Trails are added via a POST request to /add_trail.

Example: { "trail_name": "Forest Walk", "trail_length": 5.2 }
Inserts data into the trails table using:
sql
Copy code
INSERT INTO [CW2].[trails] (trail_name, trail_length) VALUES (?, ?)
Flask Routes

Organized in manage_users.py and manage_trails.py using Flask blueprints.
Allows easy scaling and modular development.
Templates

HTML templates render data dynamically for routes like /get_users.
🗄 Database Design
Tables
users

user_id (Primary Key, Auto-increment)
user_name (VARCHAR)
trails

trail_id (Primary Key, Auto-increment)
trail_name (VARCHAR)
trail_length (FLOAT)
📂 File Structure

├── app.py                    # Main Flask app
├── database/
│   ├── database.py           # Functions to interact with the database
├── routes/
│   ├── manage_users.py       # Routes for user management
│   ├── manage_trails.py      # Routes for trail management
├── templates/
│   ├── get_users.html        # Template to display user data - Testing purposes
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation


bash
git clone REPO
cd REPO_Folder
Install dependencies:
  flask
  results

Set up your SQL Server database:

Create the COMP2001_CW2 database.
Add users and trails tables as per the schema above.
Run the application:

Add a user:
bash
Copy code
curl -X POST http://127.0.0.1:5000/add_user -H "Content-Type: application/json" -d '{"user_name": "Alice"}'
Add a trail:
bash
Copy code
curl -X POST http://127.0.0.1:5000/add_trail -H "Content-Type: application/json" -d '{"trail_name": "Mountain Trail", "trail_length": 10.5}'
Get all users: Access http://127.0.0.1:5000/get_users in your browser.
🔑 Key Files
database.py:

Contains all database interaction logic (e.g., add_user, add_trail, get_users).
manage_users.py:

Handles /add_user and /get_users endpoints.
manage_trails.py:

Handles /add_trail endpoint.
get_users.html:

Renders a list of users using Flask's template engine.
📝 Future Improvements
Add more robust error handling.
Include detailed logs for debugging.
Expand API endpoints to support trail retrieval and updates.
