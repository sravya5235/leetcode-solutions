class Solution:
    def getDescentPeriods(self, prices):
        ans = 1          # the first day counts as a descent period
        streak = 1       # length of current descent
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                streak += 1
            else:
                streak = 1
            ans += streak
        
        return ans
