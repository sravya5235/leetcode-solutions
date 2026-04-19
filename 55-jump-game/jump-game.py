class Solution:
    def canJump(self, a: List[int]) -> bool:
        n = len(a)
        if n <= 1:
            return True
        mx = 0
        i = 0
        while i <= mx:
            j = i + a[i]
            if j > mx:
                mx = j
            if mx >= n - 1:
                return True
            i += 1
        return False