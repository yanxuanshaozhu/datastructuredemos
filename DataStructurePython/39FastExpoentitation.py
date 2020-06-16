def fastmodel(a: int, n: int, p: int) -> int:
    if n == 0:
        return 1
    t = (a ** 2) % p
    temp = fastmodel(t, n // 2, p)
    if (n & 1) == 1:
        temp = (temp * a) % p
    return temp


if __name__ == "__main__":
    print(fastmodel(3, 1254906, 10))
