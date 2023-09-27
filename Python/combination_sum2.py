class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        s_candidates = sorted(candidates)

        def backtracking(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return 
            if i >= len(s_candidates) or total > target:
                return
            
            subset.append(s_candidates[i])
            backtracking(i+1, subset, total + s_candidates[i])
            subset.pop()
            while (i+1 < len(s_candidates) and s_candidates[i] == s_candidates[i+1]):
                i += 1
            backtracking(i+1, subset, total)

        backtracking(0, [], 0)
        return res

    # Time Complexity: O(n*n!)
    # Space Complexity: O(n!)
    # Datastructure(s): Arrays
    # Algorithm(s): DFS, Backtracking
    # Pattern: DFS, Backtracking
    
    ### 
    # Solve Description: Similar to combination_sum, use recursive DFS to backtrack all
    #   possible combinations. However, before DFS, sort the candidates from least to 
    #   greatest in order to group duplicate values. Stopping criteria is the same as 
    #   combination sum. However, before recursing the subset without the current candidate, 
    #   increment the next candidate integer until the next candidate value does not equal
    #   the current candidate. 
    ###
    
    # Link: https://leetcode.com/problems/combination-sum-ii/