# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Add an array to store sum values
        sums = [0]
        
        # Assume maximum sum is last element in prices
        _max = prices[-1]
        
        # Traversing from the end of the list,
        for i in range(len(prices)-1, 0, -1):
            if _max < prices[i-1]:
                # Under this condition, we set _max value to prices[i-1] because,
                # We want maximum day to sell the stock
                _max = prices[i-1]
            elif _max >= prices[i-1]:
                # Under this condition, we remove that value from the _max value because,
                # If we buy on this day and sell on _max day, we get profit.
                sums.append(_max - prices[i-1])

        # In various profits, we want max one, so max(sums)
        return max(sums)
