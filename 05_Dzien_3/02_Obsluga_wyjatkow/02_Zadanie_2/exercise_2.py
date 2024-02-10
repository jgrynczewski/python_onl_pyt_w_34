from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    str_num = input("Enter number:")
    num = int(str_num)
    if num == rnd:
        print("Great!")
        guessed = True
    else:
        print("Wrong!")
