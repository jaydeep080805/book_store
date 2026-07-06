from flask import Flask, render_template, request, redirect, session
from database_connection import DatabaseConnection
from lib.books.book_repository import BookRepository
from lib.users.user_repository import UserRepository
from login_required import login_required_decorator
from flask_bcrypt import Bcrypt

# instantiate a Flask app object
app = Flask(__name__)

app.secret_key = "some_really_secret_key"
bcrypt = Bcrypt(app)


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"


# duplicate route
# @app.route('/hello', methods=['GET'])
# def hello_again():
#     return "Hello, hello and hello again!"

@app.route("/seed-db", methods=["GET"])
def seed_db():
    conn = DatabaseConnection()
    conn.connect()

    conn.seed("seeds/books.sql")

    return "<h1>seeded database<h1/>"


@app.route("/", methods=["GET"])
def index():
    # conn = DatabaseConnection()
    # conn.connect()

    # book_repo = BookRepository(conn)


    # print("Books:")

    # for book in book_repo.all():
    #     print(f"{book.id}: {book.title} - {book.author}")

    return render_template("index.html")


@app.route("/books", methods=["GET"])
def books():
    conn = DatabaseConnection()
    conn.connect()

    book_repo = BookRepository(conn)
    all_books = book_repo.all()

    return render_template("books/books.html", books=all_books)

@app.route("/books", methods=["POST"])
@login_required_decorator
def create_book():
    new_book = request.form

    conn = DatabaseConnection()
    conn.connect()

    book_repo = BookRepository(conn)
    book_repo.create(new_book)
    
    return redirect("/books")

@app.route("/authors", methods=["GET"])
def authors():
    return [
        {
            "name": "Julia Donaldson",
            "dob": "1948-09-16"
        },
        {
            "name": "Andrea Beaty",
            "dob": "1961-10-08"
        },
        {
            "name": "Kelly Barnhill",
            "dob": "1973-01-01"
        },
        {
            "name": "Zetta Elliott",
            "dob": "1979-11-11"
        }
    ]

@app.route("/sign-up", methods=["GET"])
def sign_up():
    return render_template("users/sign_up.html")

@app.route("/sign-up", methods=["POST"])
def create_user():
    form_data = request.form
    
    conn = DatabaseConnection()
    conn.connect()
    user_repo = UserRepository(conn, bcrypt)

    user_repo.create_user(form_data)

    return redirect("/users")

@app.route("/users", methods=["GET"])
def users():
    conn = DatabaseConnection()
    conn.connect()

    user_repo = UserRepository(conn, bcrypt)

    users = user_repo.all()

    return render_template("users/users.html", users=users)


@app.route("/login", methods=["GET"])
def login_route():
    return render_template("users/login.html")

@app.route("/session", methods=["POST"])
def login():
    form_data = request.form
    username = form_data.get("username")
    password = form_data.get("password")
    
    conn = DatabaseConnection()
    conn.connect()
    user_repo = UserRepository(conn, bcrypt)

    user_exists = user_repo.does_user_exist(username)
    # print(user_exists)

    if user_exists == True:
        if user_repo.check_password(username, password) == True:
            session["username"] = username
            return redirect("/users")

    return redirect("/login")


# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(port=5001, debug=True, host="0.0.0.0")
