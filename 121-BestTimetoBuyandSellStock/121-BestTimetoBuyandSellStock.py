class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        prev_lowest = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > prev_lowest:
                curr_profit = prices[i] - prev_lowest
                max_profit = curr_profit if curr_profit > max_profit else max_profit
            elif prices[i] < prev_lowest:
                prev_lowest = prices[i]

        return max_profit
        