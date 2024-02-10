![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1

Napisz funkcję `make_tuple`, która przyjmie cztery parametry: `a`, `b`, `c` i `d`. Niech parametry `c` i `d` 
bedą opcjonalne i ich standardowe wartości będą wynosiły odpowiednio 3 i 4. Zwróć krotkę czterech elementów, 
której kolejnymi elementami będą wartości parametrów.

##### Przykład:

```python
a = make_tuple("mama", "tata")
print(a)
```
```
('mama', 'tata', 3, 4)
```
```python
a = make_tuple(0, 0, 0, 0)
print(a)
```
```
(0, 0, 0, 0)
```


## Zadanie 2

Napisz funkcję `find_first_and_last`, która przyjmie listę lub krotkę. Następnie zwróć krotkę,
która będzie zawierać pierwszy i ostatni element parametru.


## Zadanie 3

Napisz funkcję `format_date`, która przyjmie 3 parametry:

* `day`: dzień,
* `month`: miesiąc,
* `year`: rok.

Funkcja powinna sprawdzić, czy data jest poprawna: 
* miesiąc powinen być w granicach (1, 12),
* dzień nie może być większy od 30 - 31 (lub 28 w przypadku lutego, pomiń sprawdzanie lat przestępnych).

Jeśli któryś z warunków będzie niezgodzny z kalendarzem, funkcja ma zwrócić `None`.  

Funkcja powinna zwrócić sformatowany łańcuch tekstowy w formacie "dzień miesiąc rok".

##### Przykład

```python
d = format_date(12, 1, 2017)
print(d)
```
```
12 stycznia 2017
```
```python
d = format_date(12, 13, 2017)
print(d)
```
```
None
```


## Zadanie 4

Napisz funkcję `find_boundaries`, która przyjmie listę liczb. 
Funkcja powinna zwrócić krotkę z najmniejszą i największą liczbą w zestawie. 
Jeśli na liście będzie element, nie będący liczbą, powinien zostać zignorowany. 
W przypadku wprowadzenia pustej listy, funkcja powinna zwrócić `None`.

##### Przykład:
```python
b = find_boundaries([1, 5, 2, 3.5, -1])
print(b)
```
```
(-1, 5)
```
```python
b = find_boundaries([0, 2, "a kuku!", 10])
print(b)
```
```
(0, 10)
```


## Zadanie 5

Napisz funkcję `censor`, która przyjmie jako parametr dowolnie długi łańcuch tekstowy. Następnie:

* rozbije łańcuch tekstowy na listę wyrazów,
* sprawdzi, czy nie znajdują się w nim słowa niedozwolone,
* jeśli tak -- zamieni je na cztery gwiazdki (`****`)
* ponownie połączy listę w string i zwróci wartość.

##### Słowa niedozwolone:
*Java*, *C#*, *Ruby*, *PHP*. 
(zwróć uwagę na wielkość znaków np. 'PhP' **nie** powinno być ocenzurowane)

Słowa niedozwolone trzymaj jako listę wewnątrz funkcji `censor`.

##### Przykład
```python
c = censor("Java is the best, but PHP is the bestest!")  # ;-)
print (c)
```
```
**** is the best, but **** is the bestest!
```


## Zadanie 6

Napisz funkcję `check_palindrome`, która pobierze jeden wyraz i sprawdzi, czy jest palindromem. 
Funkcja powinna zwracać `True`, jeśli łańcuch jest palindromem, `False`, jeśli nie jest.
