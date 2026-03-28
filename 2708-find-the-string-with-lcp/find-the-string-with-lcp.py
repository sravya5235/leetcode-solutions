class Solution:
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def findPar(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.findPar(self.parent[x])
            return self.parent[x]

        def unite(self, x, y):
            px = self.findPar(x)
            py = self.findPar(y)

            if px == py:
                return

            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px
            else:
                self.parent[px] = py
                self.rank[py] += 1

    def compute(self, word, dp):
        n = len(word)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i + 1 < n and j + 1 < n:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0

    def findTheString(self, lcp):
        n = len(lcp)
        dsu = self.DSU(n)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    dsu.unite(i, j)

        grp = [''] * n
        word = ['?'] * n
        c = ord('a')

        for i in range(n):
            p = dsu.findPar(i)
            if grp[p] == '':
                if c > ord('z'):
                    return ""
                grp[p] = chr(c)
                c += 1
            word[i] = grp[p]

        for i in range(n):
            for j in range(n):
                if lcp[i][j] == 0 and word[i] == word[j]:
                    return ""

        dp = [[0] * n for _ in range(n)]
        self.compute(word, dp)

        if dp == lcp:
            return "".join(word)
        return ""