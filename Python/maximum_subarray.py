class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Kadane's Algorithm
        current_max, overall_max = 0, -inf
        for n in nums:
            current_max = max(n, current_max + n) # Check if n > current_max + n. 
            overall_max = max(overall_max, current_max) # Check if current_max > overall_max
        return overall_max

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Arrays & Hashing
    
    ###
    # Solve Description: Loop through nums array. If the value of the current num is greater than the prefix current_max
    #   value, replace current_max with the current num. Otherwise, add current num to current_max. Then, check if the
    #   current_max is greater than the overall_max, updating it if it is. 
    ###
    
    # Link: https://leetcode.com/problems/maximum-subarray/
