# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # if preorder and inorder lists are empty, return none
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) # the first elem in preorder is always the root node for given tree/subtree
        mid = inorder.index(preorder[0]) # get the index of the root in inorder to find partitions
        
        # calculate the subtrees to recurse on
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) # +1 for preorder is for starting after root
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Binary Tree, Array
    # Algorithm(s): None
    # Pattern: Tree, Recursion

    ###
    # Solve Description: The intuition for solving this problem is that
    #   the preorder describes the order of the nodes from top down whereas
    #   the inorder describes the position of the left and right children nodes 
    #   of a given node. First, create a root node from the first element in 
    #   preorder list. Then, get the index of the root value in the inorder list
    #   and set it to a variable mid. Then, perform recursive search on left and 
    #   right subtrees. For the left subtree, pass the left subarrays of preorder and inorder
    #   such that they contain only children of the root using the root index stored 
    #   in mid. Do the same for the right subtree, except pass the right subarrays of preorder
    #   and inorder. 
    ###
    
    # Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/