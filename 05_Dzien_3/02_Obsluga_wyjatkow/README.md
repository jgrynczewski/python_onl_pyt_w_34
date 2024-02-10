![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 - rozwiązywane z wykładowcą

Napisz funkcję `safe_get`, która przyjmue dwa parametry:

* `l`: dowolna lista,
* `index`: liczba.

Funkcja powinna zwracać element listy o indeksie `index`. Jeśli nie ma takiego elementu, powinna zwracać `None`. 

**uwaga:** zrób to używając obsługi wyjątków.


## Zadanie 2

W pliku **exercise2.py** znajdziesz prostą zgadywankę: komputer losuje liczbę od 1 do 10, po czym każe Ci ją zgadnąć. 
Przeanalizuj kod. Uruchom program. Spróbuj wpisać błędną daną i zobacz, jak w takiej sytuacji zachowuje się program. 

Popraw kod tak, aby po wpisaniu nieprawidłowej wartości nie zakończył działania komunikatem błedu, 
ale poinformował użytkownika o błędzie i kontynuował działanie. 

*Podpowiedź: Zobacz jaki wyjątek jest zgłaszany i odpowiednio go obsłuż.* 


## Zadanie 3

Napisz funkcję `divide`, która przyjmie dwa argumenty: `a` i `b`. Muszą być to liczby naturalne. 
Funkcja ma działać następująco:

* ma sprawdzić, czy `a` i `b` to liczby,
* ma obsłużyć problem dzielenia przez zero.

Oba powyższe przypadki muszą być obsłużone przez wychwytywanie wyjątków.

Jeśli któryś z powyższych (nieprawidłowych) przypadków nie zostanie spełniony, funkcja ma zwrócić `None`.


## Zadanie 4

Napisz funkcję `phone`, która przyjmie parametr `number`, który oznacza numer telefonu. 
Funkcja ma sprawdzić, czy podany numer znajduje się na liście numerów (wymyśl jakieś). 
Jeśli tak – niech zwróci numer podany w parametrze. Jeśli nie - musi zwrócić wyjątek typu `Exception` z komentarzem 
`Nie ma takiego numeru!`.
