# import lib  # i wtedy lib.message
from lib import message


input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}
result = message(input_dict)
print(result)

input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
