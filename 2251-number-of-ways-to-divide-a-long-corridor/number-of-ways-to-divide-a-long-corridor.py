class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = []
        for i, c in enumerate(corridor):
            if c == 'S':
                seats.append(i)
        
        # Must have an even number of seats, and at least 2
        if len(seats) % 2 == 1 or len(seats) == 0:
            return 0
        
        ways = 1
        
        # For every completed pair, begin checking the gap
        # seats grouped as: (0,1), (2,3), (4,5), ...
        for i in range(2, len(seats), 2):
            # gap between end of previous pair and start of this pair
            prev_end = seats[i-1]
            next_start = seats[i]
            ways = (ways * (next_start - prev_end)) % MOD
        
        return ways
