import sqlite3

# Connect to the database - creates the file if it doesn't exist
def get_connection():
    # sqlite3.connect() opens the database file
    # if the file does not exist, Python creates it automatically
    connection = sqlite3.connect("access_control.db")
    # return the connection so other functions can use it
    return connection

# Create the table if it doesn't exist
def create_table():
    # get the database connection
    connection = get_connection()
    # cursor is what actually runs SQL commands
    # think of it like Postman but for databases
    cursor = connection.cursor()
    # execute runs the SQL command
    # CREATE TABLE IF NOT EXISTS means only create if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- database assigns ID automatically
            name TEXT NOT NULL,                    -- name must be a string, cannot be empty
            access TEXT NOT NULL,                  -- access value, cannot be empty
            has_access INTEGER NOT NULL            -- 1 = True, 0 = False in SQLite
        )
    """)
    # commit saves the changes to the database permanently
    connection.commit()
    # close the connection when done - good practice
    connection.close()


    # Insert a new user record into the database
def insert_user(name, access, has_access):
    # get the database connection
    connection = get_connection()
    # cursor runs the SQL command
    cursor = connection.cursor()
    # INSERT INTO adds a new row to the users table
    # the ? marks are placeholders - never put values directly in SQL strings
    # this protects against SQL injection attacks
    cursor.execute("""
        INSERT INTO users (name, access, has_access)
        VALUES (?, ?, ?)
    """, (name, access, has_access))
    # save the changes
    connection.commit()
    # close the connection
    connection.close()

# Get all users from the database
def get_all_users():
    # get the database connection
    connection = get_connection()
    # cursor runs the SQL command
    cursor = connection.cursor()
    # SELECT * means get all columns
    # FROM users means from the users table
    cursor.execute("SELECT * FROM users")
    # fetchall() returns all rows as a list
    rows = cursor.fetchall()
    # close the connection
    connection.close()
    # return all the rows
    return rows