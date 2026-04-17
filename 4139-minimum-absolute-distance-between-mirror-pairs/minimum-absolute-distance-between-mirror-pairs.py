class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reversion(x):
            res = 0
            while x > 0:
                x, d = divmod(x, 10)
                res = 10 * res + d
            return res
        hash_map = {}
        mod = inf 
        for i, x in enumerate(nums):
            rev = reversion(x)
            if x in hash_map:
                mod = min(mod, i - hash_map[x])
            hash_map[rev] = i
        return -1 if mod == inf else mod