def multiply(string1: str, string2: str) -> int:
    length = len(string1) + len(string2)
    ls = [0] * length
    for i in range(len(string1)):
        for j in range(len(string2)):
            temp = int(string1[i]) * int(string2[j])
            ls[i + j + 1] += temp % 10
            ls[i + j] += temp // 10
    for k in range(length - 1, 0, -1):
        if ls[k] >= 10:
            temp = ls[k]
            ls[k] = temp % 10
            ls[k - 1] += temp // 10
    first = ls[0]
    while first == 0 and len(ls) > 1:
        ls.pop(0)
        first = ls[0]
    return "".join([str(x) for x in ls])


if __name__ == "__main__":
    print(multiply("999", "999"))
    print(999 * 999)
