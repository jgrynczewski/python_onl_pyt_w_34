![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Podstawy programowania w Pythonie &ndash; egzamin próbny.

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

##### Odpowiedzi na pytania programistyczne umieszczaj w odpowiednich plikach *answers1.py* &ndash; *answer6.py*

**Powodzenia!**

----------------------------------------------------------------------------------------

## Zadanie 1. (2pkt)

Napisz funkcję `shorten`, która przyjmie dowolnie długi napis, po czym zwróci skrót napisu, jak w przykładzie:

```python
shortened = shorten("Don't repeat yourself")
print(shortened)
```
```
DRY
```
```python
shortened = shorten("Read the fine manual")
print(shortened)
```
```
RTFM
```
```python
shortened = shorten("All terrain armoured transport")
print(shortened)
```
```
ATAT
```

---

## Zadanie 2. (3pkt)

Napisz funkcję `name_sorter`, która przyjmie jako parametr listę imion. 

Funkcja ma zwrócić słownik:
* klucz o nazwie `male` ma mieć jako wartość imiona męskie z listy wejściowej,
* klucz o nazwie `female` ma mieć jako wartość imiona żeńskie z listy wejściowej.

Dodatkowo, posortuj imiona w ramach swoich list.

Należy przyjąć, że imiona żeńskie, to te, które kończą się literą "a". Barnabę możemy spokojnie zignorować. ;-)

**Przykład:**
```python
names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))
```

```
{'female': ['Alicja', 'Barbara'], 'male': ['Andrzej', 'Cezary', 'Henryk']}
```

---

## Zadanie 3. (3pkt)

Napisz funkcję `check_palindrome`, która pobierze dowolnie długi łańcuch tekstowy i sprawdzi, czy jest palindromem. 
Funkcja powinna zwracać `True`, jeśli łańcuch jest palindromem, `False`, jeśli nie jest.

##### Podpowiedzi:
1. Palindrom to słowo lub zdanie, które czytane wspak brzmi tak samo, jak od początku, np. "kajak", "radar", czy 
"Kobyła ma mały bok".

2. Podczas sprawdzania palindromu, pamiętaj o spacjach.

---

## Zadanie 4. (3pkt)

Napisz funkcję `div`, która przyjmie 2 argumenty liczbowe. Argumenty to początek i koniec zakresu liczb. 
Funkcja ma jako wynik, zwrócić listę liczb w podanym zakresie, które jednocześnie są podzielne przez 2 
i niepodzielne przez 3.
Wprowadzony zakres powinien być domknięty, tzn. należy sprawdzić także liczby, które są początkiem i końcem zakresu.


##### Przykład:
```python
result = div(0, 20)
print(result)
```
```
[2, 4, 8, 10, 14, 16, 20]
```

---

#### Zadanie 5. (4pkt)

Napisz funkcję `roll`, która przyjmie 3 parametry: 

* liczbę kostek, 
* opcjonalnie: typ kostki (dozwolone kostki 3, 4, 6, 8, 10, 12 i 100 ścienne), standardowa wartość, to **6** ,
* opcjonalnie: modyfikator wyniku (liczba dodana, lub odjęta od wyniku kośćmi), standardowa wartość, to **0**.

Następnie funkcja ma zasymulować rzut odpowiednią liczbą kostek, zsumować wyniki i dodać (lub odjąć) modyfikator. Wynik ma zwrócić.

Dla uproszczenia możesz przyjąć, że wszystkie liczby podane jako parametry są liczbami naturalnymi.

Jeśli użytkownik wpisze kostkę, której nie ma w powyższym zestawieniu, funkcja ma wyrzucić wyjątek `Exception` z komunikatem "No such dice!" 


##### Podpowiedź
```python
roll(2, 10, 20)  # rzut 2 kostkami 10-ściennymi, do wyniku dodać 20
roll(3, 6, -3)  # rzut 3 kostkami 6-ściennymi, od wyniku odjąć 3
```

---

## Zadanie 6. (5pkt)

 Zapoznaj się z modułem `exam` umieszczonym w pliku dołączonym do tego egzaminu. W tym module znajduje się słownik `movies`, w którym można znaleźć listę ulubionych i znienawidzonych filmów pewnego programisty. 

 Używając Flaska, utwórz stronę, którą udostępnisz pod adresem `/movies`:
 
 * jeśli użytkownik wejdzie na stronę metodą GET, wyświetl formularz, który:
    * będzie miał pole tekstowe o nazwie `title`,
    * opisem pola będzie: "Insert title",

* jeśli użytkownik wejdzie na stronę metodą POST:
    * sprawdź, czy film znajduje się na liście ulubionych filmów, jeśli tak, zwróć tekst "favourite",
    * sprawdź, czy film znajduje się na liście znienawidzonych filmów, jeśli tak, zwróć tekst "hated",
    * jeśli nie znajduje się na żadnej liście, zwróć tekst "no such movie!".
    
**Ważne:** Powołując aplikację Flaska, użyj zmiennej `app`!
