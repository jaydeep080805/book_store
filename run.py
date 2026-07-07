from app.application_factory import create_app
from flask import render_template

app = create_app()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5001, debug=True, host="0.0.0.0")
