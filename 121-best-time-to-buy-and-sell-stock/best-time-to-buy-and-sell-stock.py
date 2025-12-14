class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Track minimum price seen so far
            if price < min_price:
                min_price = price
            else:
                # Calculate profit if sold today
                max_profit = max(max_profit, price - min_price)

        return max_profit
