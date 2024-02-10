from flask import Flask, request
from exam import movies


app = Flask(__name__)


FORM = """
<form method="POST">
    <label for="title">Insert title:</label><br>
    <input type="text" id="title" name="title"><br>
    <input type="submit" value="Submit">
</form>
"""


@app.route("/movies/", methods=("GET", "POST"))
def movies_view():
    if request.method == "GET":
        return FORM
    else:
        title = request.form.get("title")
        if title in movies["favourite"]:
            return "favourite"
        elif title in movies["hated"]:
            return "hated"
        else:
            return "no such movie!"


if __name__ == '__main__':
    app.run()
