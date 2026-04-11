import requests

def check_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"healthy | status: {response.status_code}")
        else:
            print(f"unhealthy | status: {response.status_code}")
    except Exception as e:
        print(f"unreachable | error: {e}")

environments = [
    {"name": "dev",  "url": "http://localhost:8000"},
    {"name": "test", "url": "http://localhost:8001"},
    {"name": "prod", "url": "http://localhost:8002"}
]

for env in environments:
    print(f"Checking {env['name']}...")
    check_health(env["url"])