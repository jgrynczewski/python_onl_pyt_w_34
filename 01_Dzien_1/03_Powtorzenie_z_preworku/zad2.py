import random
rows = random.randint(5,15)
columns = random.randint(5,15)

print(rows, columns)

counter = 0

while counter < rows:
    print(columns * '*')
    counter = counter + 1
