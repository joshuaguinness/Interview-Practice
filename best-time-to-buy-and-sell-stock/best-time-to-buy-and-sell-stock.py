class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # diff = [0]*len(prices)
        max_profit = 0
        min_purchase = prices[0]
        
        for i, price in enumerate(prices):
            max_profit = max(max_profit, price - min_purchase)
            min_purchase = min(min_purchase, price)
            
            # max_gain = 0
            # for j in range(i+1, len(prices)):
            #     if (max_gain < (prices[j] - price)):
            #         max_gain = (prices[j] - price)
            # diff[i] = max_gain
             
        return max_profit
        
        
        