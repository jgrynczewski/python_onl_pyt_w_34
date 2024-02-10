![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 - rozwiązywane z wykładowcą.

To zadanie ma zapoznać Was z budową funkcji i pokazać, jak działa instrukcja `return`. Wykonajcie je z wykładowcą. 
Nie wahajcie się pytać, jeśli czegoś nie rozumiecie.

* Napisz funkcję `square(num)`, która zwróci wartość `num` podniesione do kwadratu.
* Stwórz funkcję `square_print(num)`. Niech ta funkcja będzie identyczna z funkcją z punktu poprzedniego podpunktu,
 jednak zamiast zwracać (`return`), niech wypisuje wynik (`print`). 
* A teraz zróbmy test: zadeklaruj zmienną `a`, przypisz do niej wynik funkcji `square(10)` i dodaj do niego 10. 
Jaka wartość będzie w zmiennej `a`?
* Kontynuujemy test: zadeklaruj zmienną `b`, przypisz do niej wynik funkcji `square_print(10)` i dodaj do niego 10. 
Co się stało? Dlaczego tak się stało? Jeśli nie rozumiesz – zapytaj wykładowcę.


## Zadanie 2 - rozwiązywane z wykładowcą.

Napisz funkcję `multiply(subject, times)`, która zwróci wartość zmiennej `subject`
pomnożoną przez wartość argumentu `times`. 
Zwróć uwagę, co się stanie, gdy jako wartość argumentu `subject` wpiszesz liczbę, a co, jeśli string.



## Zadanie 3

Napisz funkcję `power`, która przyjmuje dwa argumenty:

* `base`: obowiązkowy,
* `exponent`: opcjonalny o standardowej wartości równej 2.

Funkcja ma zwrócić wartość `base` podniesione do potęgi `exponent`.


## Zadanie 4

Napisz funkcję `convert_to_usd`, która przyjmuje parametr `euros`, 
czyli kwotę w złotówkach. Funkcja ma zwrócić podaną kwotę w dolarach amerykańskich. 
Jako przelicznik przyjmij wartość 0,82 EUR = 1 USD. 


## Zadanie 5

Napisz funkcję `to_celsius`, która przyjmie parametr `fahrenheit`, 
czyli temperaturę w stopniach Fahrenheita. Funkcja ma przeliczyć temperaturę podaną w parametrze, 
na stopnie Celsjusza. 

Użyj wzoru: 

```
     (F - 32) * 5
C =  ------------
          9
```
gdzie:

* C – temperatura w stopniach Celsjusza,
* F – temperatura w stopniach Fahrenheita.


#### Zadanie 6

Napisz funkcję `calculate_net`, która przyjmie argumenty:

* `gross`, czyli kwotę brutto ceny zakupu,
* `vat`, czyli wartość podatku VAT. Możesz założyć, że VAT ma być liczbą zmiennoprzecinkową z zakresu 0 &ndash; 1.

 Funkcja ma zwrócić wartość netto ceny. Jakie obliczenia musisz wykonać?


## Zadanie 7

* Napisz funkcję `is_even`, która przyjmie parametr `number` – dowolną liczbę całkowitą (możesz założyć, że 
programista wprowadzi prawidłową liczbę, nie musisz tego sprawdzać). Funkcja ma **zwrócić** `True`, jeśli 
liczba jest parzysta, `False` – jeśli nie. 

**Hint:** Liczba jest parzysta, jeśli dzieli się przez 2 bez reszty. Wykorzystaj operator modulo `%`.

* Napisz funkcję `iterate_through`, która przyjmie parametr `number` (nie musisz sprawdzać poprawności). 
Następnie funkcja w pętli powinna przeitrerować od 1 do wartości `number` i sprawdzić parzystość kolejnej liczby. 
Wynik należy **wypisać** na ekranie (nie zwrócić). Do sprawdzenia parzystości wykorzystaj funkcję `is_even`, 
napisaną przed chwilą.
