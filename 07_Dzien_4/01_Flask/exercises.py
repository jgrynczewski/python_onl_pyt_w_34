from datetime import datetime
from flask import Flask


app = Flask(__name__)


# widok
@app.route("/hello/")
def hello():
    return "Hello, world!"


@app.route("/time/")
def time_view():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


@app.route("/date/")
def date_view():
    now = datetime.now()
    return now.strftime("%d %b %Y")


@app.route("/<string:name>/")
def intro_view(name):
    return f"Witaj {name.title()}!"


@app.route('/')
def home():
    return "Witaj, użytkowniku!"


@app.route('/hello/<string:name>/')
def name_view(name):
    return f"{name}"


@app.route('/licz/<int:num1>/<int:num2>/')
def add_view(num1, num2):
    return f"{num1 + num2}"


if __name__ == "__main__":
    app.run(debug=True)
