def find_boundaries(numbers):
    if not numbers:
        return None

    min_value = numbers[0]
    max_value = numbers[0]
    for number in numbers:
        if type(number) == int or type(number) == float:
            if number < min_value:
                min_value = number
            if number > max_value:
                max_value = number

    return min_value, max_value


result = find_boundaries([1, 5, 2, 3.5, -1])
print(result)

b = find_boundaries([0, 2, "a kuku!", 10])
print(b)
