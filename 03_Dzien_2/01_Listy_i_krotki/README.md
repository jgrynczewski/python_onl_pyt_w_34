![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 - rozwiązywane z wykładowcą

Napisz funkcję `create_list`, która przyjmie dwa argumenty dowolnego typu, a następnie zwróci listę, 
której kolejne elementy będą parametrami powtórzonymi czterokrotnie.

##### Przykład:

```python
my_list = create_list(1, 2)  # wynik: [1, 2, 1, 2, 1, 2, 1, 2]
my_list_2 = create_list(True, False)  # wynik: [True, False, True, False, True, False, True, False]
```


## Zadanie 2 - rozwiązywane z wykładowcą

Napisz funkcję `list_keys(d)`, gdzie `d` to dowolny słownik. Niech funkcja przeiteruje pętlą **for** po kluczach 
słownika i zwróci listę tych kluczy. Sprawdź w dokumentacji, czy można zrobić to prościej.


## Zadanie 3

Napisz funkcję `find_short_words`, która przyjmie listę wyrazów. 
Funkcja powinna zwrócić listę słów krótszych od 5 znaków.

##### Przykład
```python
l = find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])
print(l)
```
```
['moja', 'ty', 'jak']
```


## Zadanie 4

Napisz funkcję `suma(numbers)` gdzie `numbers` to lista liczb dowolnego typu. 
Funkcja powinna zwrócić sumę wszystkichh elementów listy `numbers`. Dla uproszczenia możesz przyjąć, 
że wszystkie parametry wprowadzone przez programistę będą poprawnymi liczbami.

**Uwaga:** funkcję nazywamy nieco niepoprawnie (po polsku) i robimy to świadomie! 
Nie możemy nazwać funkcji `sum()` ponieważ taka funkcja już istnieje w standardzie języka Python.


## Zadanie 5

Napisz funkcję `mean(numbers)`, gdzie `numbers` to lista liczb dowolnego typu. 
Funkcja powinna zwrócić średnią arytmetyczną wszystkich elementów listy numbers. 
Czy znasz jakiś sposób, by ułatwić sobie pracę?
