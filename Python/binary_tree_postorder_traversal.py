# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def postorderDFS(node):
            if not node:
                return
            
            postorderDFS(node.left)
            postorderDFS(node.right)
            res.append(node.val)

        postorderDFS(root)
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Tree
    # Algorithm(s): none
    # Pattern: Tree
    
    # Link: https://leetcode.com/problems/binary-tree-postorder-traversal/