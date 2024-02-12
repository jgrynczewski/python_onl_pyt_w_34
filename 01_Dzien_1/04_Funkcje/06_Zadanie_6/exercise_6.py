def is_even(number):
    if number % 2 == 0:
        return True

    return False


def iterate_through(number):
    counter = 0
    while counter < number:

        if is_even(counter):
            print("Liczba", counter, "jest parzysta.")
        else:
            print("Liczba", counter, "jest nieparzysta.")

        counter = counter + 1
