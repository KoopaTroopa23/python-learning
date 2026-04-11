import requests
import time

def check_health(name, url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        duration = round(time.time() - start, 2)

        if response.status_code == 200:
            print(f"{name} is healthy | status: {response.status_code} | response time: {duration}s")
        else:
            print(f"{name} is unhealthy | status: {response.status_code}")

    except Exception as e:
        print(f"{name} is unreachable | error: {e}")

environments = [
    {"name": "dev", "url": "http://localhost:8000"},
    {"name": "test", "url": "http://localhost:8001"},
    {"name": "prod", "url": "http://localhost:8002"}
]

for env in environments:
    check_health(env["name"], env["url"])