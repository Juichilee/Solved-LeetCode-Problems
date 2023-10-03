class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::]) # same as subset.copy()
                return
            
            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # all subsets that do not include nums[i] 
            # skip nums that equal nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

    # Time Complexity: O(n*2^n)
    # Space Complexity: O(2^n)
    # Datastructure(s): Arrays
    # Algorithm(s): DFS, Backtracking
    # Pattern: DFS, Backtracking
    
    ###
    # Solution Description: Use recursive backtracking to solve. The stop condition should
    #   be when the current index is equal to the length of nums, in which case the currently
    #   tracked subset should be added to the results list. Before searching, add the current
    #   num at index i to the current subset. Then, perform recursive search on the next index,
    #   popping the current num from the subset when the recursive search returns. Then,
    #   to perform the backtracking to find the subsets that do not include the current num,
    #   increment the current index until it points to a number that != current num. Then,
    #   perform another recursive search on the new index. 
    ###
    
    # Link: https://leetcode.com/problems/subsets-ii/
    