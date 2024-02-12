# use case: Filtr na listy parzyste
list_ = [1, 2, 3, 4, 55, 23]

idx = 0
result = []

while idx < len(list_):
    item = list_[idx]
    if item % 2 == 0:
        result.append(item)

    idx = idx + 1

print(result)

