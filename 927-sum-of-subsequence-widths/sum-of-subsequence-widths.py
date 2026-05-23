class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        return sum(((1 << i) - (1 << len(nums) - i - 1)) * a for i, a in enumerate(sorted(nums))) % (10 ** 9 + 7)