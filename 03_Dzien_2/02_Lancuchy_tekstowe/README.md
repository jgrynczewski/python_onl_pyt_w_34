![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1

Napisz funkcję `message`, która jako parametr przyjmie słownik o następujących kluczach:

* **name**,
* **role**,
* **movie**.

Następnie niech funkcja przygotuje sformatowany napis: "In _movie_, _name_ is a _role_.",
gdzie w odpowiednie miejsca podstawi wartości z ww. kluczy.
Jeśli któregoś z kluczy nie będzie w słowniku, funkcja ma zwrócić wartość `None`.

##### Przykład:

```python
input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))
```

##### Wynik:
```plaintext
In Star Wars, Han Solo is a smuggler.
```
```python
input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
```

##### Wynik:
```plaintext
None
```
