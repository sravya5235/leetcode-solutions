class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxSum = 0
        lsum = 0
        rsum = 0
        for i in range(k):
            lsum += cardPoints[i]
        maxSum = lsum
        ridx = len(cardPoints) - 1
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[ridx]
            ridx = ridx - 1
            maxSum = max(maxSum, lsum + rsum)
        return maxSum