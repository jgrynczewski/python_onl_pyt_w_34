def find_short_words(words_list):
    idx = 0
    result = []
    while idx < len(words_list):
        item = words_list[idx]
        if len(item) < 5:
            result = result + [item]

        idx = idx + 1
    return result


l = find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])
print(l)
