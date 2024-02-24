# functions in python are firs-class citizens
#                         -------------------


def deco(func):
    def modified_func():
        print("Witaj!")
        func()

    return modified_func


@deco
def message():
    print("ala ma kota")


# message = deco(message)
message()
