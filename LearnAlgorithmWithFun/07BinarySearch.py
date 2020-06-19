def binarysearch1(ls: list, target: object) -> bool:
    ls = sorted(ls)
    start = 0
    end = len(ls) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == ls[mid]:
            return True
        elif target < ls[mid]:
            end = mid - 1
        elif target > ls[mid]:
            start = mid + 1
    return False


def binarysearch2(ls: list, target: object) -> bool:
    ls = sorted(ls)
    if len(ls) == 0:
        return False
    else:
        mid = len(ls) // 2
        if target == ls[mid]:
            return True
        else:
            if target < ls[mid]:
                return binarysearch2(ls[:mid], item)
            elif target > ls[mid]:
                return binarysearch2(ls[mid + 1:], item)


if __name__ == "__main__":
    ls1 = [60, 17, 39, 15, 8, 34, 30, 45, 5, 52, 25]
    item = 1
    print(binarysearch1(ls1, item))
    print(binarysearch2(ls1,item))
