import pyodbc

# Function to establish a database connection
def get_database_connection():
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"  # Connect to localhost
        "Database=COMP2001_CW2;"  # Specify the database name
        "UID=SA;"  # User ID
        "PWD=C0mp2001!;"  # Password
    )
    return conn

# Function to add a user
def add_user(user_name):
    connection = get_database_connection()
    cursor = connection.cursor()

    query = "INSERT INTO [CW2].[users] (user_name) VALUES (?)"
    cursor.execute(query, (user_name,))
    connection.commit()

    cursor.close()
    connection.close()

# Function to fetch all users
def get_users():
    connection = get_database_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM [CW2].[users]"
    cursor.execute(query)
    users = cursor.fetchall()

    cursor.close()
    connection.close()
    return users

# Function to add a trail
def add_trail(trail_name, trail_length):
    connection = get_database_connection()
    cursor = connection.cursor()

    # Insert the trail into the trails table
    query = "INSERT INTO [CW2].[trails] (trail_name, trail_length) VALUES (?, ?)"
    cursor.execute(query, (trail_name, trail_length))
    connection.commit()

    cursor.close()
    connection.close()