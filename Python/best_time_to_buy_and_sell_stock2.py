class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Edge case: cannot be profit if only 1 price
        if len(prices) == 1:
            return 0

        buy_idx = 0
        total_profit = 0

        while (buy_idx < len(prices)):
            sell_idx = buy_idx + 1 
            max_profit = 0
            # Loop as long as the sell_idx is within prices and the profit between buy_idx and sell_idx is positive
            while (sell_idx < len(prices) and prices[buy_idx] < prices[sell_idx]):
                buy_price = prices[buy_idx]
                sell_price = prices[sell_idx]
                curr_profit = sell_price - buy_price

                if curr_profit > max_profit:
                    sell_idx += 1
                    max_profit = curr_profit
                else:
                    break # Break out of the current buy sell loop if profit is not strictly increasing
                
            total_profit += max_profit
            buy_idx = sell_idx
        
        return total_profit

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Array
    # Algorithm(s): None
    # Pattern: Sliding Window
    
    ###
    # Solve Description: Use sliding window to calculate profit between
    #   buy and sell points. To maximize profits, only add to total profits
    #   when the value of the stock strictly increases on consecutive days.
    #   Use two pointers, buy_idx and sell_idx to keep track of buy and sell days.
    ###
    
    # Link: https://leetcode.com/problems/binary-tree-inorder-traversal/