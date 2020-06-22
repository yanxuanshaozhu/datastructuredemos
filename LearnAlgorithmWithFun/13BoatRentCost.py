def calcost(decks: list) -> tuple:
    n = len(decks)
    cost = [[0] * n for _ in range(n)]
    path = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cost[i][j] = decks[i][j]
    for d in range(3, n + 1):
        for i in range(0, n - d + 1):
            j = i + d - 1
            for k in range(i + 1, j):
                temp = cost[i][k] + cost[k][j]
                if temp < cost[i][j]:
                    cost[i][j] = temp
                    path[i][j] = k

    ls = []

    def travel(start: int, end: int) -> list:
        mid = path[start][end]
        if mid != 0:
            ls.append(mid)
            travel(start, mid)
            travel(mid, end)
        return ls

    ls = travel(0, n - 1) + [0, n - 1]
    ls.sort()
    return cost[0][n - 1], ls


if __name__ == "__main__":
    inputs = [[0, 2, 6, 9, 15, 20],
              [0, 0, 3, 5, 11, 18],
              [0, 0, 0, 3, 6, 12],
              [0, 0, 0, 0, 5, 8],
              [0, 0, 0, 0, 0, 6],
              [0, 0, 0, 0, 0, 0]]
    a, b = calcost(inputs)
    print(a)
    print(b)
