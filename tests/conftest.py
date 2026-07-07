import pytest
from ..database_connection import DatabaseConnection
from flask import Flask
from flask_bcrypt import Bcrypt
# from ..application_factory import create_app

# @pytest.fixture()
# def app():
#     app = create_app()
#     app.config.update({
#         "TESTING": True,
#     })

#     yield app


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture
def db():
    conn = DatabaseConnection()
    conn.connect()

    conn.seed("seeds/users.sql")
    conn.seed("seeds/books.sql")
    conn.seed("seeds/movies.sql")

    return conn

@pytest.fixture
def bcrypt():
    app = Flask(__name__)
    return Bcrypt(app)