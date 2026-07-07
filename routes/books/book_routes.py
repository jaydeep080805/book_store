from flask import Blueprint, render_template, request, redirect
from database_connection import DatabaseConnection
# from ...lib.books.book_repository import BookRepository
from lib.books.book_repository import BookRepository
from login_required import login_required_decorator

book_route = Blueprint('book_route', __name__,
                        template_folder='templates')

@book_route.route("/books", methods=["GET"])
def books():
    conn = DatabaseConnection()
    conn.connect()

    book_repo = BookRepository(conn)
    all_books = book_repo.all()

    return render_template("books/books.html", books=all_books)

@book_route.route("/books", methods=["POST"])
@login_required_decorator
def create_book():
    new_book = request.form

    conn = DatabaseConnection()
    conn.connect()

    book_repo = BookRepository(conn)
    book_repo.create(new_book)
    
    return redirect("/books")

@book_route.route("/authors", methods=["GET"])
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