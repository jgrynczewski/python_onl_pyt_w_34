def create_list(param1, param2):
    result = [param1, param2] * 4
    return result


my_list = create_list(1, 2)  # wynik: [1, 2, 1, 2, 1, 2, 1, 2]
my_list_2 = create_list(True, False)  # wynik: [True, False, True, False, True, False, True, False]

print(my_list)
print(my_list_2)
