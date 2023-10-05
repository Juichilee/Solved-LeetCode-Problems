class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit
            
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Sliding Window
    
    ###
    # Solve Description: Initialize left and right pointers to index 0 and 1. 
    #   Keep the right pointer incrementing through the prices list. Calculate 
    #   the current profit by subtracting the prices at right index from left index. 
    #   If the profit is positive and is greater than max profit, update max profit. 
    #   Otherwise, set the left index to the right index
    ###
    
    # Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
            