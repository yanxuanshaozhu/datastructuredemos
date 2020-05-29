def transform(num):
    ls = []
    s = ""
    while num > 0:
        temp = num % 2
        ls.append(temp)
        num = num // 2
    while len(ls) > 0:
        s += str(ls.pop())
    return s


if __name__ == "__main__":
    print(transform(10))
