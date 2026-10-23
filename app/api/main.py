# Import FastAPI class from the fastapi library
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel    # Python library that validates data - UserAccess
from app.api.database import create_table, insert_user, get_all_users, update_user    # Sqlite Database

# Create an instance of the FastAPI app
# This is the main application object
app = FastAPI()

# Create the database table when the app starts
create_table()

# Root endpoint - returns HTML landing page
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Access Control API</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 80px auto; padding: 20px; background: #f5f5f5; }
            h1 { color: #2E75B6; }
            .status { color: green; font-weight: bold; }
            .btn { display: inline-block; margin: 10px 5px; padding: 10px 20px; background: #2E75B6; color: white; text-decoration: none; border-radius: 5px; }
            .btn:hover { background: #1a5a96; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }
            th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
            th { background: #2E75B6; color: white; }
        </style>
    </head>
    <body>
        <h1>Access Control API</h1>
        <p>Status: <span class="status">● Running</span></p>
        <p>Version: 1.0.0</p>

        <a class="btn" href="/docs">Swagger UI Docs</a>
        <a class="btn" href="/access">View All Users</a>
        <a class="btn" href="/health">Health Check</a>

        <table>
            <tr><th>Method</th><th>Endpoint</th><th>Description</th></tr>
            <tr><td>GET</td><td>/</td><td>This page</td></tr>
            <tr><td>GET</td><td>/health</td><td>Health check</td></tr>
            <tr><td>GET</td><td>/user/{name}</td><td>Get user by name</td></tr>
            <tr><td>POST</td><td>/access</td><td>Create user access record</td></tr>
            <tr><td>GET</td><td>/access</td><td>Get all user records</td></tr>
            <tr><td>PUT</td><td>/access/{name}?access=...</td><td>Change a user's access</td></tr>
        </table>
    </body>
    </html>
    """

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# This endpoint accepts a variable in the URL called "name"
# Example: if someone calls /user/Kevin, name will equal "Kevin"
@app.get("/user/{name}")
def get_user(name: str):
    # name: str means name must be a string - this is called type hinting
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

@app.put("/access/{name}")
def update_access(name: str, access: str):
    # Change a user's access in the database - no code edit needed
    # Example: PUT /access/Addie?access=not granted
    has_access = access.strip().lower() == "granted"
    changed = update_user(name, access, int(has_access))
    if changed == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"name": name, "access": access, "has_access": has_access}

from mangum import Mangum
handler = Mangum(app)