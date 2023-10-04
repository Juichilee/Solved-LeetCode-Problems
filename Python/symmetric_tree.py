# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q = collections.deque()

        q.append(root)

        # perform bfs
        while q:
            qLen = len(q)
            compare = [] # add all nodes in level to compare list to check symmetry
            for i in range(qLen): # pop all nodes in q for current breadth level
                node = q.popleft()
                if not node:
                    compare.append(None)
                if node:
                    compare.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            l, r = 0, len(compare)-1 # use two pointers to compare items starting at both ends of compare
            while l < r:
                if compare[l] != compare[r]:
                    return False
                l += 1
                r -= 1
        return True
            
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Tree
    # Algorithm(s): BFS
    # Pattern: Tree, BFS, Two Pointer
                
    ###
    # Solve Description: Use BFS to check if all nodes are symmetrical at any given depth. 
    #   Instantiate a deque to store all nodes at a given depth. For a given depth,
    #   pop all nodes from deque, appending their children to the other end of the dequeue and
    #   adding the popped nodes to a compare list. Then, using two pointers l and r, compare the value of
    #   the nodes at each end of the compare list, incrementing the pointers to move towards the center.
    #   If the values of two opposing nodes do not match, then return False.
    ###
    
    # Link: https://leetcode.com/problems/symmetric-tree/



        