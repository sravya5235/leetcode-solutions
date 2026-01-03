class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        aba = 6
        abc = 6
        for _ in range(n - 1):
            na = (3 * aba + 2 * abc) % mod
            nb = (2 * aba + 2 * abc) % mod
            aba, abc = na, nb        
        return (aba + abc) % mod
