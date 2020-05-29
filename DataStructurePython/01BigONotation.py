import time


def test1():
    ls1 = []
    for i in range(100000):
        ls1 = ls1 + [i]


def test2():
    ls2 = []
    for i in range(100000):
        ls2.append(i)


def test3():
    ls3 = [i for i in range(100000)]


def test4():
    ls4 = list(range(100000))


start = time.time()
test1()
end = time.time()
print("1: ", end - start)

start = time.time()
test2()
end = time.time()
print("2: ", end - start)

start = time.time()
test3()
end = time.time()
print("3:", end - start)

start = time.time()
test4()
end = time.time()
print("4:", end - start)
