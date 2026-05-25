class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        lowest_buy = 0
        max_profit = 0

        while sell < len(prices):

            if prices[sell] > prices[buy]:
                current_profit = prices[sell] - prices[buy]
                max_profit = max(current_profit, max_profit)
            else:
                buy = sell
            
            sell += 1
        
        return max_profit