def name_sorter(names):
    """Sort words and separate singular and plural.

    :param list words: list of words
    :rtype: dict
    :return: dict with separate words.
    """
    result = {
        'singulars': [],
        'plurals': []
    }

    for name in names:
        if name[-1] == 's':
            result['plurals'].append(name)
        else:
            result['singulars'].append(name)
    return result


if __name__ == '__main__':
    input_data = ["tomato", "tomatoes", "potato", "potatoes", "cars", "unicorns", "horse", "cow"]
    print(name_sorter(input_data))
