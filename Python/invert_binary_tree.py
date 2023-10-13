# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.switchLeftRight(root)
    
    def switchLeftRight(self, node):
        if not node:
            return None 
        
        nodeLeft = self.switchLeftRight(node.left)
        nodeRight = self.switchLeftRight(node.right)

        tempLeft = nodeLeft
        node.left = nodeRight
        node.right = tempLeft

        return node

    # Time Complexity: O(n)
    # Space ComplexitY: O(1)
    # Datastructure(s): Tree
    # Algorithm(s): None
    # Pattern: Recursion

    # Link: https://leetcode.com/problems/invert-binary-tree/



