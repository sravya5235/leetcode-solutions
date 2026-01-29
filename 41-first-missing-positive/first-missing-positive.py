class Solution(object):
    def firstMissingPositive(self, nums: List[int]) -> int:
        num = max(nums)
        nums = set(nums)
        for i in range(1, num):
            if i not in nums:
                return i

        if num < 0:
            return 1
        else:
            return num+1
        