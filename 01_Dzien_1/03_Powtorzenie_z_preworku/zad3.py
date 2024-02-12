import random

size = random.randint(3, 9)
print("Wielkość choinki:", size)

counter1 = 0
while counter1 < size+1:

    counter2 = 0
    row = ""
    while counter2 < size:
        row = row + "*"
        i = counter2 + 1

    counter1 = counter1 + 1
