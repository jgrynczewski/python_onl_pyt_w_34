PHONE_BOOK = [
    '123456789',
    '987654321'
]


def phone(number):
    if number not in PHONE_BOOK:
        raise Exception("Nie ma takiego numeru!")

    return number


phone('12343452')
