def suma(numbers):
    return sum(numbers)


def suma1(numbers):
    suma_ = 0
    for number in numbers:
        suma_ = suma_ + number
    return suma_


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(suma1(numbers))
print(suma(numbers))
