def divide(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError):
        return None


res = divide(3, 0)
print(res)
