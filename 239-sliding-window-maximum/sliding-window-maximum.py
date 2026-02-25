from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []
        
        for i in range(len(nums)):
            
            # 1️⃣ Remove elements out of window
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # 2️⃣ Maintain decreasing order
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            
            # 3️⃣ Add current index
            dq.append(i)
            
            # 4️⃣ Add max to result
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result