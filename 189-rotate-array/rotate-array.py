from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle k > n
        
        # Helper function to reverse portion of array
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # Step 1: Reverse entire array
        reverse(0, n - 1)
        
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse remaining elements
        reverse(k, n - 1)