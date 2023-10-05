# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, currentSum):

            if not node.left and not node.right and currentSum == targetSum:
                return True
            
            if not node.left and not node.right:
                return False
            
            leftRes, rightRes = False, False
            if node.left:
                leftRes = dfs(node.left, node.left.val + currentSum)
            if node.right:
                rightRes = dfs(node.right, node.right.val + currentSum)

            return (leftRes or rightRes)
            
        return dfs(root, root.val)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Tree
    # Algorithm(s): DFS, Pre-order
    # Pattern: Tree

    ###
    # Solve Description: Check for edgecase that root is null. Use a recursive function
    #   that keeps track of the currentSum of the current node. For base cases, if the 
    #   current node is a leaf node and the currentSum == targetSum, return True, otherwise, 
    #   return False. Then, if the current node's left or right nodes exist, traverse them 
    #   while passing in the new currentSum. At the end, return the union of the truth values 
    #   from traversing the left and right subtrees 
    ###
    
    # LinK: https://leetcode.com/problems/path-sum/
