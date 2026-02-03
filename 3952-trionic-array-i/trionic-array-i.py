class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        i = 0

        # first increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # p must be at least 1
        if i == 0:
            return False

        # second decreasing
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1

        # must actually decrease
        if j == i:
            return False

        # third increasing
        k = j
        while k + 1 < n and nums[k] < nums[k + 1]:
            k += 1

        # must reach the end and q must be < n-1
        return k == n - 1 and j < n - 1
