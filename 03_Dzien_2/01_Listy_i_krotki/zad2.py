def list_keys(d):
    keys = []
    for key in d:
        keys.append(key)
    return keys


dict_ = {
    'a': 1,
    'b': 2,
    'dog': 5,
    'c': 3,
}
result = list_keys(dict_)
print(result)
