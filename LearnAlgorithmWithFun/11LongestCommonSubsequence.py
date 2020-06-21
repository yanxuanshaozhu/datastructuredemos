# LeetCode1143

import numpy as np


def lcs(string1: str, string2: str) -> tuple:
    nrow = len(string1) + 1
    ncol = len(string2) + 1
    c = np.zeros((nrow, ncol), dtype='int8')
    b = np.zeros((nrow, ncol))
    for i in range(1, nrow):
        for j in range(1, ncol):
            if string1[i - 1] == string2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            else:
                if c[i][j - 1] >= c[i - 1][j]:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = 2
                else:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = 3

    ls = []

    def path(row: int, col: int) -> list:
        if b[row][col] == 1:
            ls.append(string1[row - 1])
            path(row - 1, col - 1)
        elif b[row][col] == 2:
            path(row, col - 1)
        elif b[row][col] == 3:
            path(row - 1, col)
        ls.reverse()
        return "".join(ls)

    return c[-1][-1], path(nrow - 1, ncol - 1)


if __name__ == "__main__":
    m, n = lcs("abcadab", "bacdba")
    print(m)
    print(n)
