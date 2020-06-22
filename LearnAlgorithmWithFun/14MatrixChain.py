# Find the minimum times of  multiplication of a chain of matrices


def times(shape: list) -> tuple:
    num = len(shape) - 1
    dp = [[0] * num for _ in range(num)]
    path = [[0] * num for _ in range(num)]
    for d in range(2, num + 1):
        for i in range(0, num - d + 1):
            j = i + d - 1
            # Since d > = 2, assign dp[i][j] an initial value,otherwise it's always 0,
            # so that the following temp < dp[i][j] statement can work
            dp[i][j] = dp[i][i] + dp[i + 1][j] + shape[i] * shape[i + 1] * shape[j + 1]
            path[i][j] = i
            for k in range(i + 1, j):
                temp = dp[i][k] + dp[k + 1][j] + shape[i] * shape[k + 1] * shape[j + 1]
                if temp < dp[i][j]:
                    dp[i][j] = temp
                    path[i][j] = k
    ls = []

    def travel(start: int, end: int) -> str:
        if start == end:
            ls.append("A[" + str(start) + "]")
            return "".join(ls)
        ls.append("(")
        travel(start, path[start][end])
        travel(path[start][end] + 1, end)
        ls.append(")")
        return "".join(ls)

    return dp[0][num - 1], travel(0, num - 1)


if __name__ == "__main__":
    inputs = [3, 5, 10, 8, 2, 4]
    a, b = times(inputs)
    print(a)
    print(b)
