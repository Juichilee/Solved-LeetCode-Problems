# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Edgecase: if both p and q are empty
        if not p and not q:
            return True
        # Edgecase: if either p or q is empty or if their root node val are not the same
        if not p or not q or p.val != q.val:
            return False

        # Recursive Depth First Search 
        return (self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))

    # Time Complexity: O(p+q)
    # Space ComplexitY: O(1)
    # Datastructure(s): Tree
    # Algorithm(s): None
    # Pattern: Recursion
        
    ###
    # Solve Description: To check if two trees are the same, perform the same
    #   DFS search on both trees, comparing their values at each node.
    #   If the nodes or values of both trees at a particular depth search do not match, 
    #   then return False.
    ###

    # Link: https://leetcode.com/problems/same-tree/




