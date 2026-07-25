class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_lowest = prices[0]
        best_profit = 0

        for price in prices:
            #update lowest value
            curr_lowest = min(curr_lowest,price)
            
            #find/compare curr_profit with difference to lowest value
            best_profit = max(best_profit,price - curr_lowest)
            
        return best_profit