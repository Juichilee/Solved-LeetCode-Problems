# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # initialize results array and q deque for BFS
        res = []
        q = collections.deque([root])
        
        # while q is not empty... (BFS)
        while q:
            # each while loop is one level
            # initialize right most elem as none and fixed q_len
            right_side = None
            q_len = len(q)
            # loop through all elem in current q level
            for i in range(q_len):
                # get and remove latest node in level
                node = q.popleft()
                if node:
                    right_side = node # update right_side as current node
                    q.append(node.left) # add left, then right node to q
                    q.append(node.right)
            # only add non null right side vals to results array
            if right_side:
                res.append(right_side.val)

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(w) (w = largest node width of tree)
    # Datastructure(s): Deque, Array
    # Algorithm(s): BFS (Breadth-First-Search)
    # Pattern: Binary Tree

    # Link: https://leetcode.com/problems/binary-tree-right-side-view/


        