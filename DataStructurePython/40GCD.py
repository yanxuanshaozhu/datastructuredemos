def gcd1(a: int, b: int) -> int:
    if b == 0:
        return a
    elif a < b:
        return gcd1(b, a)
    else:
        return gcd1(a - b, b)


def gcd2(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd2(b, a % b)


# Find d = gcd(x,y) = ax+by,return (d,a,b)
def extgcd(x: int, y: int) -> tuple:
    if y == 0:
        return x, 1, 0
    else:
        (d, b, a) = extgcd(y, x % y)
        return d, b, a - (x // y) * b


if __name__ == "__main__":
    print(gcd1(5, 6))
    print(gcd2(5, 6))
    print(extgcd(5, 6))
