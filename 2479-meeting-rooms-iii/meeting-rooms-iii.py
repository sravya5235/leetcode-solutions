import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        available = list(range(n))
        heapq.heapify(available)
        
        used = []  # (end_time, room)
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free rooms that are done before start
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(used, (end, room))
            else:
                finish, room = heapq.heappop(used)
                heapq.heappush(used, (finish + duration, room))
            
            count[room] += 1
        
        return count.index(max(count))
