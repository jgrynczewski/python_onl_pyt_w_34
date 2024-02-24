# LBYL - Look Before You Leap (prewencja)
# if (ew. case)
# while True:
#     num = input("Podaj liczbę: ")
#
#     if not num.isdigit():
#         print("Podana wartość jest nieprawidłowego typu (podaj int).")
#     else:
#         num = int(num)
#         if num == 0:
#             print("Nie można dzielić przez 0")
#         else:
#             print(f"Wynik to: {10/num}")


# EAFP - Easier Ask Forgiveness than Permission (leczenie)
# try:
# except:
while True:
    num = input("Podaj liczbę")
    try:
        num = int(num)
        print(f"Wynik to: {10 / num}")
    except ValueError:
        print("Podana wartość jest nieprawidłowego typu (podaj int).")
        continue
    except ZeroDivisionError:
        print("Nie można dzielić przez 0")
        continue
