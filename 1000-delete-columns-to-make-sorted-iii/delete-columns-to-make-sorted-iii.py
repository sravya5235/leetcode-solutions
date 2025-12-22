class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # dp[j] = max kept columns ending at column j
        dp = [1] * m

        for j in range(m):
            for i in range(j):
                # check if column i can come before column j
                if all(strs[r][i] <= strs[r][j] for r in range(n)):
                    dp[j] = max(dp[j], dp[i] + 1)

        max_kept = max(dp)
        return m - max_kept
