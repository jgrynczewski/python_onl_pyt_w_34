def suma(numbers):
    suma_ = 0
    for number in numbers:
        suma_ = suma_ + number
    return suma_


def mean(numbers):
    return suma(numbers) / len(numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mean(numbers))
