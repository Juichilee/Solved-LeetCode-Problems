# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # recursive DFS
        def isValid(node, left_val, right_val):

            # return True if node is null
            if not node:
                return True

            # check if node is valid
            if not (node.val < right_val and node.val > left_val):
                return False

            # traverse tree depth first
            return isValid(node.left, left_val, node.val) and isValid(node.right, node.val, right_val)
        
        return isValid(root, float("-inf"), float("inf"))

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Stack, BST
    # Algorithm(s): Recursive DFS
    # Pattern: Tree, DFS, BST

    ###
    # Solve Description: Use recursive DFS to solve. Stopping condition is if
    #   the current node is null, in which case, return True as the base condition
    #   that will be propogated upwards anc checked in parent and ancestor nodes.
    #   In non-null nodes, If the parent node's value is greater than the right node or
    #   lesser than the left node, then return False. Otherwise, recurse on the left
    #   and right child nodes, comparing and returning their results when they return. 
    ###
    
    # Link: https://leetcode.com/problems/validate-binary-search-tree/