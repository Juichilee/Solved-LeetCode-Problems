class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        permutation = []

        def dfs(index, remaining):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return 
            
            for idx, current_num in enumerate(remaining):
                permutation.append(current_num)
                dfs(index + 1, remaining[:idx] + remaining[idx+1:])
                permutation.pop()

        dfs(0, nums.copy())
        return res

    # Time Complexity: O(N*N!)
    # Space ComplexitY: O(N!)
    # Datastructure(s): Arrays
    # Algorithm(s): Backtracking
    # Pattern: Arrays, Backtracking
    
    ###
    # Solve Description: Use recursive DFS to find all possible combinations of nums. 
    #   Keep a permutation array to keep track of current permutation. For stopping 
    #   criteria, if the permutation length matches the nums length, add the current
    #   permutation to results. For searching, keep a list of remaining nums allowed
    #   to be added to the permutation. Then, for each remaining num, append to current
    #   permutation and recurse on the next index. When the recursion returns, pop the
    #   recently appended num from permutation. 
    ###
    
    # Link: https://leetcode.com/problems/permutations/