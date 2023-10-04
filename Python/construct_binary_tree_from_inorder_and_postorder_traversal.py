# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # if inorder is null or postorder is null, return None, marking leaf node
        if not inorder or not postorder:
            return None
        
        # last element in postorder is the root of the current tree/subtree
        root = TreeNode(postorder.pop()) 
        # get index of root in the inorder index to separate left and right subtrees. 
        # (e.g., root=3 -> inorder [9, 3, 15, 20, 7] -> inorderLeft [9], inorderRight [15, 20, 7])
        inorderIndex = inorder.index(root.val) 

        # recursively build upon right subtree. if inorderIndex is out of bounds, inorder is []
        # following the previous case, inorder[inorderIndex+1:] == [15, 20, 7], postorder = [9, 15, 7, 20]
        root.right = self.buildTree(inorder[inorderIndex+1:], postorder) 
        # recursively build upon left subtree
        # following the previous case, inorder[:inorderIndex] == [9], postorder = [9] (after entire right subtree is completed)
        root.left = self.buildTree(inorder[:inorderIndex], postorder) 

        return root

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Tree, Binary Tree
    # Algorithm(s): DFS
    # Pattern: Tree, Binary Tree, DFS
    
    ###
    # Solve Description: See above comments.
    ###
    
    # Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/