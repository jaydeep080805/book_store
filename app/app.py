# from flask import render_template
# from database_connection import DatabaseConnection
# from application_factory import create_app

# app = create_app()


# @app.route('/hello', methods=['GET'])
# def hello():
#     return "Hello to you too"


# @app.route("/seed-db", methods=["GET"])
# def seed_db():
#     conn = DatabaseConnection()
#     conn.connect()

#     conn.seed("seeds/books.sql")

#     return "<h1>seeded database<h1/>"




# @app.route("/authors", methods=["GET"])
# def authors():
#     return [
#         {
#             "name": "Julia Donaldson",
#             "dob": "1948-09-16"
#         },
#         {
#             "name": "Andrea Beaty",
#             "dob": "1961-10-08"
#         },
#         {
#             "name": "Kelly Barnhill",
#             "dob": "1973-01-01"
#         },
#         {
#             "name": "Zetta Elliott",
#             "dob": "1979-11-11"
#         }
#     ]


# # make the server run in response to `python app.py`
# # on port 5001 (you'll learn more about what this means later)
# # and use debug mode so that changing code restarts the app
# if __name__ == "__main__":
#     app.run(port=5001, debug=True, host="0.0.0.0")
