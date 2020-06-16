# there are n kinds of package, each has a weight and a value, the sum of  weights can be at most volume c,
# each kind can be taken by an arbitrary amount which is less or equal to 1, find a plan to max the total value


def take(weights: list, values: list, volume: int) -> tuple:
    vpw = []
    for i in range(len(weights)):
        vpw.append((values[i] / weights[i], values[i], weights[i]))
    ls = sorted(vpw, key=lambda x: x[0])
    tv = 0
    sm = 0
    amount = 0
    items = []
    while sm != volume:
        item = ls.pop()
        if sm + item[2] < volume:
            sm += item[2]
            tv += item[1]
            amount += 1
            items.append((item[1], item[2], 1))
        elif sm + item[2] >= volume:
            quantity = (volume - sm) / item[2]
            sm = volume
            tv += quantity * item[1]
            amount += quantity
            items.append((item[1], item[2], quantity))
    return tv, sm, items


if __name__ == "__main__":
    a, b, c = take([4, 2, 9, 5, 5, 8, 5, 4, 5, 5, ], [
        3, 8, 18, 6, 8, 20, 5, 6, 7, 15], 30)
    print(a)
    print(b)
    print(c)
