# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative DFS Solution
        curr = root # current node being traversed and processed after stack pop
        stack = [] # stack for storing nodes for iterative DFS
        n = 0 # counter for tracking current ordered number

        # end while if cur is null and stack is empty
        while curr or stack:
            # while curr is not null, add curr to stack and go left
            while (curr):
                stack.append(curr)
                curr = curr.left
            
            # if curr is null, remove parent node from stack and process it
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            
            # go down the right side to check for null or more left subtrees to process
            curr = curr.right

    # Time Complexity: O(n)
    # Space Complexity: O(d) (d = max depth of tree)
    # Datastructure(s): Stack, BST
    # Algorithm(s): Iterative DFS
    # Pattern: Tree, DFS, BST
    
    # Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Recursive Solution:
        # def BSTtoOrderedList(node):

        #     # if node is null, return an empty list
        #     if not node:
        #         return []

        #     # traverse left and right
        #     left_list = BSTtoOrderedList(node.left)
        #     right_list = BSTtoOrderedList(node.right)

        #     # add left and right list and node val to form ordered array
        #     return left_list + [node.val] + right_list

        # # orderedList from smallest to greatest
        # orderedList = BSTtoOrderedList(root)

        # # return the kth smallest element from 0-indexed orderedList
        # return orderedList[k-1]



