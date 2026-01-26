class Solution:
    def partition(self, s: str):
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # Precompute palindrome table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        res = []
        path = []

        def backtrack(start):
            if start == n:
                res.append(path[:])
                return

            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res
