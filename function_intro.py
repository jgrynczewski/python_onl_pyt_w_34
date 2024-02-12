# DRY (Don't Repeat Yourself)

def func(animal, name, x):
    print(name, "ma", animal)
    x = x + 1
    return x


result = func("kota", "Ala", 4)

print("Hello")
print(result)
z = 3

func("papugę", "Tomek", 10)

y = 6
print("Cześć")

func("psa", "Franek", 3)

print("Cośtam")
print("Cośtam")
