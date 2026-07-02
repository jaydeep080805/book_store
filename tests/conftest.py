import pytest
from ..database_connection import DatabaseConnection

@pytest.fixture
def db():
    conn = DatabaseConnection()
    conn.connect()

    conn.seed("seeds/users.sql")
    conn.seed("seeds/books.sql")

    return conn
