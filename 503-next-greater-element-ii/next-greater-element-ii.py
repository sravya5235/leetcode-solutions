from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # stores indices
        
        # Traverse twice
        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i % n]
            
            if i < n:
                stack.append(i)
        
        return result