class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Related to Kadane's algorithm for "largest sum contiguous subarray" problem
        # intuition: max subarray has to be a prefix or suffix of the array given no 0's and odd number of negative numbers
        prefix, suffix, max_so_far = 0, 0, float('-inf') # prefix/suffix keep track of product
        for i in range(len(nums)):
            # purpose of 'or 1' resets the product to 1 for following nums when 0 is encountered
            prefix = (prefix or 1) * nums[i] 
            suffix = (suffix or 1) * nums[~i]
            max_so_far = max(max_so_far, prefix, suffix) # find and update the max of all 3
        return max_so_far
            
        # Space Optimized DP Solution:
        # def maxProduct(self, nums: List[int]) -> int:
        # maxi = mini = ans = nums[0]
        # for i in nums[1:]:
        #     maxi, mini = max(i, i*maxi, i*mini), min(i, i*maxi, i*mini)
        #     ans = max(ans, maxi)
        # return ans

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Arrays
    # Algorithm(s): Kadane's Algorithm
    # Pattern: Arrays, DP
    
    # Link: https://leetcode.com/problems/maximum-product-subarray/