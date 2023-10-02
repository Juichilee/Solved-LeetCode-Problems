class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i] (LEFT)
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i] (RIGHT)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    # Time Complexity: O(n*2^n)
    # Space Complexity: O(2^n)
    # Datastructure(s): Arrays
    # Algorithm(s): DFS, Backtracking
    # Pattern: DFS, Backtracking
    
    ###
    # Solution Description: Initialize an array called 'subset' to keep track of the current
    #   nums subset. Use DFS using 'i' to track the current nums index being processed.
    #   Stop condition is if 'i' is no longer a valid index (greater than equal to len(nums))
    #   in which case, add a copy of the 'subset' array so far. For the search, there are two
    #   cases to recurse upon: the subset with the current num[i] included and the subset without
    #   it included.
    ###
    
    # Link: https://leetcode.com/problems/subsets/