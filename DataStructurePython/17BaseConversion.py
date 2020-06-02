def baseConversion(num: int, base: int) -> str:
    standard = "0123456789ABCDEF"
    if num < base:
        return standard[num]
    else:
        return baseConversion(num // base, base) + standard[num % base]


if __name__ == "__main__":
    temp = baseConversion(10,2)
    print(temp[::])
