import os
import sqlite3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.pool import NullPool


def _build_engine():
    # Render injects DATABASE_URL (Postgres) in production via render.yaml.
    url = os.environ.get("DATABASE_URL")
    if url:
        # Render/Heroku-style URLs use the "postgres://" scheme, but
        # SQLAlchemy needs a driver-qualified scheme.
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+psycopg://", 1)
        elif url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+psycopg://", 1)
        return create_engine(url, poolclass=NullPool)

    # Local dev fallback: no Postgres install required. SQLAlchemy normally
    # resolves a relative sqlite path to an absolute one at the first
    # connection and keeps using that, which breaks tests that chdir into a
    # fresh tmp_path per test. A creator callable defers the real
    # sqlite3.connect() (and its path resolution) to each actual connect.
    return create_engine(
        "sqlite://",
        creator=lambda: sqlite3.connect("access_control.db"),
        poolclass=NullPool,
    )


engine = _build_engine()
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("access", String, nullable=False),
    Column("has_access", Integer, nullable=False),
)


# Create the table if it doesn't exist
def create_table():
    metadata.create_all(engine)


# Insert a new user record into the database
def insert_user(name, access, has_access):
    with engine.begin() as connection:
        connection.execute(
            users.insert().values(name=name, access=access, has_access=has_access)
        )


# Get all users from the database
def get_all_users():
    with engine.connect() as connection:
        result = connection.execute(users.select())
        return [tuple(row) for row in result]


# Change access for an existing user (matched by name)
# returns the number of rows changed (0 = no such user)
def update_user(name, access, has_access):
    with engine.begin() as connection:
        result = connection.execute(
            users.update()
            .where(users.c.name == name)
            .values(access=access, has_access=has_access)
        )
        return result.rowcount
