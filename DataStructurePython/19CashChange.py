def change1(coins: [], amount: int) -> int:
    minnum = amount
    if amount in coins:
        return 1
    else:
        for ele in [element for element in coins if element <= amount]:
            num = 1 + change1(coins, amount - ele)
            if num < minnum:
                minnum = num
    return minnum


def change2(coins: [], amount: int, result: []) -> int:
    minnum = amount
    if amount in coins:
        result[amount] = 1
        return 1
    elif result[amount] > 0:
        return result[amount]
    else:
        for ele in [element for element in coins if element <= amount]:
            num = 1 + change2(coins, amount - ele, result)
            if num < minnum:
                minnum = num
                result[amount] = minnum
    return minnum


if __name__ == "__main__":
    import time

    start1 = time.time()
    print(change1([1, 5, 10, 25], 63))
    end1 = time.time()
    print("method1: ", end1 - start1)

    start2 = time.time()
    print(change2([1, 5, 10, 25], 63, [0] * 64))
    end2 = time.time()
    print("method2: ", end2 - start2)
