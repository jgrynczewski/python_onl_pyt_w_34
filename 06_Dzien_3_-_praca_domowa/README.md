![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1

Napisz funkcję `random_average(n)`, która wylosuje `n` liczb naturalnych od 1 do 100, zsumuje je, 
po czym zwróci średnią arytmetyczną z tych liczb.

Ze względu na konstrukcję testów automatycznych użyj w zadaniu poniższej formy importu funkcji `randint`:

```python
import random
```

a następnie w kodzie używaj konstrukcji:

```python
random.randint()
```


## Zadanie 2

Napisz funkcję `div`, która:

* poprosi użytkownika o podanie 2 liczb z klawiatury,
* wprowadzone dane zamieni na liczby naturalne,
* podzieli jedną liczbę przez drugą,
* wyświetli wynik.

Dodatkowo należy zabezpieczyć się przed wszystkimi możliwymi błędami (niewłaściwe dane, dzielenie przez zero). 

Sprawdź w interaktywnej konsoli Pythona, jakie błędy mogą wystąpić i zabezpiecz się przed nimi.


## Zadanie 3(*): Sprawdzanie poprawności numeru PESEL

Napisz funkcję `validate_pesel`, która przyjmie numer PESEL jako łańcuch tekstowy, po czym sprawdzi jego poprawność 
i zwróci:

* `True`, jeśli PESEL jest poprawny,
* `False`, jeśli PESEL jest błędny.

##### Zasady walidacji numeru PESEL

PESEL składa się z 11 cyfr, z czego ostatnia jest cyfrą kontrolną. Aby sprawdzić PESEL, należy:

* pierwsze dziesięć cyfr pomnożyć przez odpowiednią _wagę_, 
* otrzymane iloczyny zsumować,
* sumę podzielić modulo 10,
* wynik dodawania odjąć od 10, jeśli wynik będzie wynosił 10, należy wziąć 0.

Jeżeli wynik powyższej operacji będzie równy ostatniej cyfrze numeru PESEL, cały numer jest poprawny.

##### Wagi:

`1 3 7 9 1 3 7 9 1 3`


##### Przykład:
Chcemy sprawdzić PESEL 44051401358. Zgodnie z procedurą, sprawdzamy dziesięć pierwszych cyfr, 
ostatnia (8) jest cyfrą kontrolną.

|         |   |    |   |    |   |    |   |   |   |    |
|---------|---|----|---|----|---|----|---|---|---|----|
| **cyfra**   | 4 | 4  | 0 | 5  | 1 | 4  | 0 | 1 | 3 | 5  | 
| **waga**  | 1 | 3  | 7 | 9  | 1 | 3  | 7 | 9 | 1 | 3  |
| **iloczyn** | 4 | 12 | 0 | 45 | 1 | 12 | 0 | 9 | 3 | 15 |

Sumujemy iloczyny: 4 + 12 + 0 + 45 + 1 + 12 + 0 + 9 + 3 + 15 = **101**

Sumę dzielimy modulo 10: 101 % 10 = **1**

Wynik dzielenia modulo odejmujemy od 10: 10 - 1 = **9**.

Podana w PESEL-u cyfra kontrolna wynosi **8**, zatem PESEL jest błędny.
