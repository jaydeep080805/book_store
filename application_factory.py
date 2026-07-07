from flask import Flask
from flask_bcrypt import Bcrypt

from routes.books.book_routes import book_route

# from routes.books.book_routes import book_route
from routes.users.user_routes import user_route
from routes.movies.movie_routes import movie_route

def create_app():
    app = Flask(__name__)

    app = Flask(__name__)

    app.secret_key = "some_really_secret_key"
    bcrypt = Bcrypt(app)
    app.bcrypt = bcrypt

    app.register_blueprint(book_route)
    app.register_blueprint(user_route)
    app.register_blueprint(movie_route)

    return app
