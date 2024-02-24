def message(d):
    if 'name' not in d or 'role'not in d or 'movie' not in d:
        return None

    # Formatowanie napisów w pythonie
    # res = 'In ' + d['movie'] + ', ' + d['name'] + ' is a ' + d['role'] + '.'  # using concatenation
    # res = "In {}, {} is {}.".format(d['movie'], d['name'], d['role'])  # Java like
    # res = "In %s, %s is %s." % (d['movie'], d['name'], d['role'])  # C like
    res = f"In {d['movie']}, {d['name']} is {d['role']}."  # f-string
    return res


if __name__ == "__main__":
    print("Ala ma kota")
    result = message({})
    print(result)
