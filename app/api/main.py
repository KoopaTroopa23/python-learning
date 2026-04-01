# Import FastAPI class from the fastapi library
from fastapi import FastAPI

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



#  FASTAPI - is like Swagger UI
#  Flask and Django is like Spring Boot