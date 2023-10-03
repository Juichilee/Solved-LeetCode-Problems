# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def inorderDFS(node):
            if not node:
                return
            
            inorderDFS(node.left)
            res.append(node.val)
            inorderDFS(node.right)

        inorderDFS(root)
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Tree
    # Algorithm(s): none
    # Pattern: Tree
    
    ###
    # Solve Description: Use recursion to perform inorder DFS. The stop
    #   condition is if the current node is null. The search conditions
    #   are to recursively search the left node, append the results of the
    #   current node to the results, and then recursively search on the right node. 
    ###
    
    # Link: https://leetcode.com/problems/binary-tree-inorder-traversal/