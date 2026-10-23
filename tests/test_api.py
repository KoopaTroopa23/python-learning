import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(tmp_path, monkeypatch):
    # The database path is relative, so run each test in an empty temp folder.
    # That way tests never touch the real access_control.db.
    monkeypatch.chdir(tmp_path)
    from app.api import database
    from app.api.main import app

    database.create_table()
    return TestClient(app)


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_create_and_read_user(client):
    created = client.post("/access", json={"name": "Kevin", "access": "granted"})
    assert created.json()["has_access"] is True

    users = client.get("/access").json()["users"]
    assert users[0]["name"] == "Kevin"
    assert users[0]["has_access"] is True


def test_put_changes_access(client):
    client.post("/access", json={"name": "Addie", "access": "granted"})
    changed = client.put("/access/Addie", params={"access": "not granted"})
    assert changed.status_code == 200
    assert changed.json()["has_access"] is False
    assert client.get("/access").json()["users"][0]["has_access"] is False


def test_put_unknown_user_returns_404(client):
    assert client.put("/access/Nobody", params={"access": "granted"}).status_code == 404
