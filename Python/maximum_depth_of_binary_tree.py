# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.countDepth(root, 0)
    
    def countDepth(self, node, depth):
        if not node:
            return depth 
        
        depth += 1
        leftDepth = self.countDepth(node.left, depth)
        rightDepth = self.countDepth(node.right, depth)

        return max(leftDepth, rightDepth)

    # Time Complexity: O(n)
    # Space ComplexitY: O(1)
    # Datastructure(s): Tree
    # Algorithm(s): None
    # Pattern: Recursion, DFS
    
    ###
    # Solve Description: Use DFS to traverse tree nodes. 
    #   For each recursive call to a node, increment depth
    #   variable by 1. When returning from having reached leaf node,
    #   return the greater depth between two child nodes. 
    ###
    
    # Link: 