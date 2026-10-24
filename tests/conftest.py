import os

# Tests must always exercise the SQLite fallback path (a fresh file per
# test, via tmp_path + monkeypatch.chdir) regardless of a developer's
# local .env pointing at a real Postgres instance. Setting -- not
# deleting -- the var to an empty string, before any test module imports
# app.api.database, stops that module's load_dotenv() call from refilling
# it from .env (load_dotenv only fills in vars that are completely absent).
os.environ["DATABASE_URL"] = ""
