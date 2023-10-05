# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root
        
        return helper(0, len(nums) - 1)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Tree
    # Algorithm(s): DFS, Pre-Order
    # Pattern: Tree

    ### 
    # Solve Description: Use a recursive helper function for pre-order traversal. 
    #   For each subtree, calculate and generate the root node by finding the mid 
    #   value between l and r pointers. Continue traversing down the left and right 
    #   subtrees, passing in the updated l and r pointers to the left or right of mid value
    ###
    
    # Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/