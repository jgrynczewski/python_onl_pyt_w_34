def message(d):
    if 'name' not in d or 'role'not in d or 'movie' not in d:
        return None

    # Formatowanie napisów w pythonie
    # res = 'In ' + d['movie'] + ', ' + d['name'] + ' is a ' + d['role'] + '.'  # using concatenation
    # res = "In {}, {} is {}.".format(d['movie'], d['name'], d['role'])  # Java like
    # res = "In %s, %s is %s." % (d['movie'], d['name'], d['role'])  # C like
    res = f"In {d['movie']}, {d['name']} is {d['role']}."  # f-string
    return res


input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}
result = message(input_dict)
print(result)

input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
