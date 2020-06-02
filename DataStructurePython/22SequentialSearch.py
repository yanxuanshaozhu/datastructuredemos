def unsortedsearch(elements: list, item: object) -> bool:
    flag = False
    pos = 0
    while pos < len(elements) and not flag:
        if elements[pos] == item:
            flag = True
        else:
            pos = pos + 1
    return flag


def sortedsearch(elements: list, item: object) -> bool:
    flag = False
    stop = False
    pos = 0
    while pos < len(elements) and not flag and not stop:
        if elements[pos] == item:
            flag = True
        else:
            if elements[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return flag


if __name__ == "__main__":
    import time

    start1 = time.time()
    print(unsortedsearch([x for x in range(10000)], 5555.5))
    end1 = time.time()
    print(end1 - start1)
    print("-----------------")
    start2 = time.time()
    print(sortedsearch([x for x in range(10000)], 5555.5))
    end2 = time.time()
    print(end2 - start2)
