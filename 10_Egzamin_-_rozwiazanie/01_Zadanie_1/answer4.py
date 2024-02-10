def div(start, end):
    """Make list with numbers divisible by 2 and not divisible by 3 from start to end (both sides included).

    :param int start: start range
    :param int end: end range
    :rtype: list
    :return: numbers from start to end divisible by 2 and not divisible by 3
    """
    return [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 != 0]


if __name__ == '__main__':
    print(div(0, 20))
