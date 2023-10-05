# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]

        # DFS recursive function
        def dfs(node):
            
            # return 0 if current node is null
            if not node:
                return 0

            # traverse sub nodes
            left = dfs(node.left)
            right = dfs(node.right)

            # calculate diff between left and right heights
            diff = abs(left - right)

            # if diff is greater than 1, return early false
            if (diff > 1):
                res[0] = False

            # return max node height
            return 1 + max(left, right)
        
        dfs(root)

        return res[0]

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): DFS
    # Pattern: Binary Tree
    
    # Link: https://leetcode.com/problems/balanced-binary-tree/