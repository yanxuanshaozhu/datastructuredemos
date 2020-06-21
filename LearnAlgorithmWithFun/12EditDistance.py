# LeetCode72

def minDistance(word1: str, word2: str) -> tuple:
    nrow = len(word1) + 1
    ncol = len(word2) + 1
    dp = [[0] * ncol for _ in range(nrow)]
    for _ in range(ncol):
        dp[0][_] = _
    for _ in range(nrow):
        dp[_][0] = _
    for i in range(1, nrow):
        for j in range(1, ncol):
            dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1,
                           dp[i - 1][j - 1] + (1 if word1[i - 1] != word2[j - 1] else 0))
    ls = []

    def path(nr: int, nc: int) -> list:
        c1 = dp[nr - 2][nc - 1] + 1
        c2 = dp[nr - 1][nc - 2] + 1
        c3 = dp[nr - 2][nc - 2] + (1 if word1[nr - 2] != word2[nc - 2] else 0)
        if c1 <= c2 and c1 <= c3:
            ls.append(("delete", word1[nr - 2]))
            path(nr - 1, nc)
        elif c2 <= c1 and c2 <= c3:
            ls.append(("insert", word2[nc - 2]))
        elif c3 <= c1 and c3 <= c2:
            if word1[nr - 2] == word2[nc - 2]:
                path(nr - 1, nc - 1)
            else:
                ls.append(("change", word1[nr - 2], "into", word2[nc - 2]))
                path(nr - 1, nc - 1)

        return ls

    return dp[-1][-1], path(nrow, ncol)


if __name__ == "__main__":
    m, n = minDistance("family", "frame")
    print(m)
    print(n)
