class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_value = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            lowest_value =  min(prices[i], lowest_value)

            profit = prices[i] - lowest_value
            max_profit =  max(max_profit, profit)

        return max_profit


        