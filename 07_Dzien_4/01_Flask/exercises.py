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


if __name__ == "__main__":
    app.run(debug=True)
