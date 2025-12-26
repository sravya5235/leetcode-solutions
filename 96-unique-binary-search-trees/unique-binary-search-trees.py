class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Empty tree
        dp[1] = 1  # Single node
        
        # Fill DP table
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]
        
        return dp[n]
