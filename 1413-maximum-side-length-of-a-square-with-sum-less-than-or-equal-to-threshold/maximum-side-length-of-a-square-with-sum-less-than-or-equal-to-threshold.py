class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = (
                    mat[i][j]
                    + prefix[i][j+1]
                    + prefix[i+1][j]
                    - prefix[i][j]
                )
        
        def exists(size):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    total = (
                        prefix[i+size][j+size]
                        - prefix[i][j+size]
                        - prefix[i+size][j]
                        + prefix[i][j]
                    )
                    if total <= threshold:
                        return True
            return False
        
        left, right = 0, min(m, n)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if exists(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
