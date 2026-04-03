import os
import requests

# Function - you know this
def check_health(url):
    # try/except - like if/else for errors
    try:
        response = requests.get(url)
        # if/else - you know this
        if response.status_code == 200:
            return "healthy"
        else:
            return "unhealthy"
    except:
        return "unreachable"

# List - you know this
environments = [
    {"name": "dev", "url": "http://localhost:8000"},
    {"name": "test", "url": "http://localhost:8001"},
]

# Loop - you know this
for env in environments:
    status = check_health(env["url"])
    print(f"{env['name']} is {status}")