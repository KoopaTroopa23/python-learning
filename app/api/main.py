# Import FastAPI class from the fastapi library
from fastapi import FastAPI
from pydantic import BaseModel    # Python library that validates data - UserAccess
from app.api.database import create_table, insert_user, get_all_users    # Sqlite Datebase

# Create an instance of the FastAPI app
# This is the main application object
app = FastAPI()

# Create the database table when the app starts
create_table()

# This is a decorator - it tells FastAPI this function handles GET requests
# The "/" means this is the root endpoint - like the homepage of the API
@app.get("/")
def read_root():
    # Return a dictionary - FastAPI automatically converts it to JSON
    return {"message": "Hello from the API",
        "fastapi_is_like": "Swagger UI",
        "flask_and_django_are_like": "Spring Boot"}

# This endpoint accepts a variable in the URL called "name"
# Example: if someone calls /user/Kevin, name will equal "Kevin"
@app.get("/user/{name}")
def get_user(name: str):
    # name: str means name must be a string - this is called type hinting
    # Return the name back in a dictionary as JSON
    return {"user": name}

# This is a model - it defines what data the POST request expects
# It is like a blueprint for the data
class UserAccess(BaseModel):
    name: str
    access: str
@app.post("/access")
def create_access(user: UserAccess):
    # Check if access is granted
    has_access = user.access.strip().lower() == "granted"
    # Save to database - convert boolean to int for SQLite
    insert_user(user.name, user.access, int(has_access))
    # Return response
    return {
        "name": user.name,
        "access": user.access,
        "has_access": has_access
    }

@app.get("/access")
def read_all_users():
    # Get all users from database
    rows = get_all_users()
    # Convert each row tuple into a dictionary
    users = [
        {"id": row[0], "name": row[1], "access": row[2], "has_access": bool(row[3])}
        for row in rows
    ]
    return {"users": users}