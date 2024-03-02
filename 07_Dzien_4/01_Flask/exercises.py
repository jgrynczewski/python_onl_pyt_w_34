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

    data = request.args  # parametry metody GET
    name = data.get("name")
    if name:
        return f"Witaj {name}!"

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


# Zad 7b - a co jeżeli to samo chcielibyśmy zrobić metodą POST ?
@app.route("/form2/", methods=["GET", "POST"])
def form_view2():

    data = request.form  # parametry metody POST
    name = data.get("name")
    if name:
        return f"Witaj {name}!"

    FORM = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <h3>Podaj swoje imię</h3>
            <form method=POST>
                <input type="text" name="name" placehloder="name">
                <input type="submit" value="Prześlij">
            </form>                
        </body>
    </html>
    """

    return FORM


# Zad 8
@app.route('/calc/')
def calc_view():

    data = request.args
    operand1 = data.get('operand1')
    operator = data.get('operator')
    operand2 = data.get('operand2')

    if operand1 and operator and operand2:
        operand1 = int(operand1)
        operand2 = int(operand2)
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        else:
            result = operand1 / operand2

        return str(result)

    FORM = """
    <form>
        <input type=number name=operand1>
        <select name=operator>
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type=number name=operand2>
        <input type=submit value=Oblicz>
    </form>
    """

    return FORM


# Zad 9
@app.route('/guess/')
def guess_view():

    data = request.args
    num = data.get('num')
    draw_param = data.get('draw')

    if not draw_param:
        draw = random.randint(1, 10)
    else:
        draw = int(draw_param)

    FORM = f"""
        <form>
            <input type=number name=num min=1 max=10 step=1>
            <input type=hidden name=draw value={draw}>
            <input type=submit value=Strzał>
        </form>
    """

    if num:
        num = int(num)
        if num > draw:
            CONTENT = "<h3>za dużo!</h3>" + FORM
        elif num < draw:
            CONTENT = "<h3>za mało!</h3>" + FORM
        else:
            CONTENT = "Gratulacje, udało Ci się!"

        return CONTENT

    CONTENT = "<h3>Spróbuj zgadnąć liczbę z przedziału 1-10</h3>" + FORM
    return CONTENT


@app.route('/zad10/', methods=["GET", "POST"])
def method_view():
    if request.method == "GET":
        return "Wysłałeś GET"
    elif request.method == "POST":
        return "Wysłałeś POST"


if __name__ == "__main__":
    app.run(debug=True)
