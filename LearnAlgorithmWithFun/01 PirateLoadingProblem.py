# The pirates want to load a number of fortunes with various weight onto their ship,and the maximum
# volume the ship can afford is c,find the maximum number of fortunes can be loaded onto the ship

import random


def load(fortunes: list, volume: int) -> tuple:
    ls = sorted(fortunes)
    sum = 0
    items = list()
    while sum <= volume:
        item = ls.pop(0)
        if sum + item > volume:
            break
        sum += item
        items.append(item)
    return items, sum


if __name__ == "__main__":
    r1, r2 = load([4, 10, 7, 11, 3, 5, 14, 2], 30)
    print(r1)
    print(r2)
