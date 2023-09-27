class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
    
    # Time Complexity: O(n*n!)
    # Space Complexity: O(n!)
    # Datastructure(s): Arrays
    # Algorithm(s): DFS, Backtracking
    # Pattern: DFS, Backtracking

    # Separate Solution
    # combo = []
    # res = []
    # res_set = set()

    # def dfs(candidates):
    #     curr_sum = sum(combo)
    #     if curr_sum > target:
    #         return
    #     if curr_sum == target:
    #         s_combo = sorted(combo)
    #         if tuple(s_combo) not in res_set:
    #             res_set.add(tuple(s_combo))
    #             res.append(s_combo)
    #         return
        
    #     for candidate in candidates:
    #         combo.append(candidate)
    #         dfs(candidates)
    #         combo.pop()
        
    # dfs(candidates)
    # return res

    # res = []

    ### 
    # Solve Description: Use recursive DFS to search through all possible combinations of 
    #   the candidates list. If the total value equals the target value, append current
    #   list combination to results array. If the current tracked index overshoots the 
    #   the length of list of candidates, return. Otherwise, add the current selected
    #   candidate to the current combination to create a new combination. Recurse on the 
    #   new combination. When the new combination recursion returns, remove the current 
    #   selected candidate from the new combination to search for new combinations without 
    #   that candidate. 
    ###
    
    # Link: https://leetcode.com/problems/combination-sum/