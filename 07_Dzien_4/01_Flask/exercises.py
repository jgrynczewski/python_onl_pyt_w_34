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



if __name__ == "__main__":
    app.run(debug=True)
