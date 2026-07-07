from flask import Blueprint, render_template, request, redirect, session, current_app
from ...login_required import login_required_decorator
from ...database_connection import DatabaseConnection
from ...lib.users.user_repository import UserRepository


user_route = Blueprint('user_route', __name__,
                    template_folder='templates')


@user_route.route("/sign-up", methods=["GET"])
def sign_up():
    return render_template("users/sign_up.html")

@user_route.route("/sign-up", methods=["POST"])
def create_user():
    bcrypt = current_app.bcrypt
    form_data = request.form
    
    conn = DatabaseConnection()
    conn.connect()
    user_repo = UserRepository(conn, bcrypt)

    user_repo.create_user(form_data)

    return redirect("/users")

@user_route.route("/users", methods=["GET"])
def users():
    bcrypt = current_app.bcrypt
    
    conn = DatabaseConnection()
    conn.connect()

    user_repo = UserRepository(conn, bcrypt)

    users = user_repo.all()

    return render_template("users/users.html", users=users)


@user_route.route("/login", methods=["GET"])
def login_route():
    return render_template("users/login.html")

@user_route.route("/session", methods=["POST"])
def login():
    bcrypt = current_app.bcrypt
    
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