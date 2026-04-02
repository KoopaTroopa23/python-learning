# Import FastAPI class from the fastapi library
from fastapi import FastAPI
from pydantic import BaseModel    # Python library that validates data - UserAccess

# Create an instance of the FastAPI app
# This is the main application object
app = FastAPI()

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
    # Check if access is granted using your ETL logic
    has_access = user.access.strip().lower() == "granted"
    return {
        "name": user.name,
        "access": user.access,
        "has_access": has_access
    }