# write the function from exercise 1 here
# pure function
def square(num):
    result = num ** 2
    return result


# side-effect function
def square_print(num):
    result = num ** 2
    print(result)


# the lines below will test your function:
print("2 squared is:", square(2))  # should be 4
print("16^2=", square(16))  # should be 256
print("256 to the 2nd power =", square(256))  # should be 65536

a = square(10) + 10
print(a)

# TypeError
# b = square_print(10) + 10
