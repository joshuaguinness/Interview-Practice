class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        
#         max_profit = 0
#         min_purchase = prices[0]
        
#         for i, price in enumerate(prices):
#             max_profit = max(max_profit, price - min_purchase)
#             min_purchase = min(min_purchase, price)
             
#         return max_profit

        # curr_purcahse = prices[0]
        # profit = 0
        
        diff = 0
        
        for i in range(len(prices)-1):
            if (prices[i+1] - prices[i] > 0):
                diff += prices[i+1] - prices[i]
                
        return diff
            # if (i == 0):
            #     continue
            # if (price > curr_purchase):
            #     # Sell
            #     profit += price - curr_purchase
            #     curr_purchase = price
            # elif (price < curr_purchase):
            #     # Buy
            # if (curr_purchase > prices[i+1]):
            #     # Sell and buy tomorrow
            #     curr_purchase = 
            
                
            
                
            