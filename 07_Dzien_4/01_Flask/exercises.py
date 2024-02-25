import random
from datetime import datetime
from flask import Flask, request


app = Flask(__name__)


# widok (intro)
@app.route("/hello/")
def hello():
    return "Hello, world!"


# Zad 2
@app.route("/time/")
def time_view():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


# Zad 3
@app.route("/date/")
def date_view():
    now = datetime.now()
    return now.strftime("%d %b %Y")


# Intro
@app.route("/<string:name>/")
def intro_view(name):
    return f"Witaj {name.title()}!"


# Zad 1
@app.route('/')
def home():
    return "Witaj, użytkowniku!"


# Zad 1
@app.route('/hello/<string:name>/')
def name_view(name):
    return f"{name}"


# Zad 4
@app.route('/licz/<int:num1>/<int:num2>/')
def add_view(num1, num2):
    return f"{num1 + num2}"


# Zad 5
@app.route("/losuj/")
def draw():
    # # one-liner
    # return " ".join([str(item) for item in random.choices(range(10), k=3)])
    nums = random.choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k=3)
    return f"{nums[0]} {nums[1]} {nums[2]}"


# Zad 6
@app.route("/lotek/")
def lotek():
    list_ = list(range(1, 50))
    random.shuffle(list_)
    result = list_[:6]
    return result


# html intro
@app.route('/welcome/')
def html_view():
    response = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <h1>Welcome!</h1>    
        </body>
    </html>
    """

    return response


# Zad 7
@app.route("/form/")
def form_view():
    data = request.args
    name = data.get("name")
    if name:
        return f"Witaj {name}!"
    else:
        FORM = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
                <h3>Podaj swoje imię</h3>
                <form>
                    <input type="text" name="name" placehloder="name">
                    <input type="submit" value="Prześlij">
                </form>                
            </body>
        </html>    
        """

        return FORM


if __name__ == "__main__":
    app.run(debug=True)
