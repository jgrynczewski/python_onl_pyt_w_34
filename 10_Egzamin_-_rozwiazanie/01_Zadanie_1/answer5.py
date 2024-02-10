import random


def roll(dices, dice_type=6, modifier=0):
    """Simulate dice roll with modifier.
    :param int dices: number of dices
    :param int dice_type: type of dices, default is 6
    :param int modifier: modifier value, default is 0

    :rtype: int
    :return: value of dice roll modified by modifier
    """
    if dice_type not in (3, 4, 6, 8, 10, 12, 100):
        raise Exception("No such dice!")
    return sum(random.randint(1, dice_type) for _ in range(dices)) + modifier


if __name__ == '__main__':
    print(roll(2))
    print(roll(4, 10, 7))
    print(roll(1, 2))
