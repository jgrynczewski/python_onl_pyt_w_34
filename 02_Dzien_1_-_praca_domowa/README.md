![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Podstawy programowania w Pythonie - zadania domowe
> Wszystkie zadania rozwiązuj w funkcjach. 
> Jeśli Twoje funkcje nie będą zwracały wartości nie będą zaliczone 
> (chyba, że jest napisane, żeby nie wykonywać działania w funkcji). 
> Każde zadanie rozwiązuj w oddzielnym pliku (np. zadanie 1. w pliku exercise_1.py, zadanie 2.
> w pliku exercise_2.py itd.)
> Możesz wypisywać w konsoli informacje, ale **nie myl tego ze zwracaniem wartości**.
> 
> Zadania z gwiazdką __(*)__ są dla chętnych
>
> Czytaj uważnie polecenia.



## Zadanie 0

Zapoznaj się z **PEP-8**. Jest to oficjalny dokument opisujący styl kodowania w Pythonie:

[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

Wracaj do niego regularnie wraz z postępem nauki i staraj się stosować do podanych tam wytycznych. 


## Zadanie 1 

(W tym zadaniu nie musisz pisać funkcji)

Napisz program, w którym zdefiniujesz wielolinijkowy łańcuch tekstowy. 
Wpisz tam zwrotkę swojego ulubionego wiersza, po czym wyświetl go na konsoli.


## Zadanie 2

Napisz funkcję o nazwie `square_area` która policzy i **zwróci** pole prostokąta 
(przyjmując dwa parametry oznaczające długość jego boków). Przyjmij, że parametry wejściowe są poprawne.


## Zadanie 3

Napisz funkcję o nazwie `circle_circuit`, która przyjmując średnicę okręgu **zwróci** jego obwód. 
Przyjmij, że parametry wejściowe są poprawne. Przyjmij `pi=3.14`.


## Zadanie 4
 
Napisz funkcję o nazwie `dogs_age`, który przeliczy wiek psa w psich latach. 

* funkcja powinna przyjmować wiek psa jako parametr,
* dla pierwszych dwóch lat, każdy rok życia psa jest równy 10.5 ludzkiego roku,
* powyżej dwóch lat, każdy rok życia psa, to 4 ludzkie lata,
* funkcja powinna **zwrócić** wiek psa.

##### Przykład:
```python
azor = dogs_age(1.5)  # spodziewany wynik: 1.5 * 10.5 = 15.75

burek = dogs_age(5)  # spodziewany wynik: 2 * 10.5 + 3 * 4 = 33
```


## Zadanie 5.

Napisz funkcję `chessboard`, który przyjmie parametr `n` jako opcjonalny. 
Standardowa wartość parametru ma wynosić 8. Funkcja ma **zwrócić** wielolinijkowy napis 
reprezentujący szachownicę złożoną ze znaków # i spacji. Szachownica powinna mieć wymiary **n x n**.

**Przykład:**
Przy n=8, szachownica powinna składać się 8 wierszy, każdy po 8 znaków, naprzemiennie # i spacja.
```python
c = chessboard()
print(c)
```
```
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # # 
```


## Zadanie 6.

Napisz funkcję `is_divisible_by_4`, która przyjmie liczbę i sprawdzi, czy liczba jest podzielna przez 4 i odpowiednio 
zwróci `True` lub `False`.


## Zadanie 7.

Napisz funkcję `histogram`, która przyjmie listę liczb, po czym **zwróci** histogram ze znaków `#`. 
Jeśli użytkownik poda wartość nie będącą liczbą, funkcja powinna zwrócić wartość `None`.

Wynikowy histogram ma być wielolinijkowym napisem składającym się ze znaków `#`. 
Jedna linijka = jeden słupek histogramu. 
> **Zadanie rozwiąż, nie korzystając z mnożenia stringów!** Zamiast tego użyj dwóch pętli.

##### Przykład:
```python
h = histogram([2, 6, 3, 1])
print(h)
```
```
##
######
###
#
```

```python
h = histogram([1, 2, 'error!'])
print(h)
```
```
None
```


## Zadanie 8(\*). Ciąg Fibonacciego.

Napisz funkcję `fib` liczącą ciąg Fibonacciego. Funkcja powinna:

* przyjmować jako parametr `n` - liczbę; ma to być element, dla którego liczymy wartość,
* zwracać wartość elementu ciągu dla elementu `n`.

##### Podpowiedź:

Ciąg Fibonacciego to ciąg liczb naturalnych. Określa się go rekurencyjnie w sposób następujący:
pierwszy element jest równy 0, drugi 1, każdy następny jest sumą dwóch poprzednich.

Sprawdź w internecie, co to jest _rekurencja_ i jak napisać funkcję, która to wykorzystuje.
