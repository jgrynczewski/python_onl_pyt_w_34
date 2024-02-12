x = 15
y = "15"

result = type(x)
result2 = type(y)

if result == int:
    print(x * 5)
elif result == float:
    print(x / 5)
elif result == str:
    print(x)

if result2 == int:
    print(y * 5)
elif result2 == float:
    print(y / 5)
elif result2 == str:
    print(y)
