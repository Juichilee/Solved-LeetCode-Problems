# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            # If p.val and q.val are both greater than cur.val, move to right node
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If p.val and q.val are both smaller than cur.val, move to left node
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # Else, if p.val or q.val is equal to p.val or q.val or cur.val is in the middle of p.val or q.val, return cur
            else:
                return cur

    # Time Complexity: O(log(n)) [height of tree]
    # Space ComplexitY: O(1)
    # Datastructure(s): Tree
    # Algorithm(s): None
    # Pattern: None
    
    # Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

    ### Alternative Solution 
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     ppath, qpath = [], []
    #     ppath = self.findNodePath(root, ppath, p)
    #     qpath = self.findNodePath(root, qpath, q)

    #     if p in qpath:
    #         return p
    #     if q in ppath:
    #         return q
    #     for nodep in ppath:
    #         if nodep in qpath:
    #             return nodep

    # def findNodePath(self, node, path, target):

    #     if not node:
    #         return None
        
    #     if node.val == target.val:
    #         path.append(node)
    #         return path

    #     leftPath = self.findNodePath(node.left, path, target)
    #     rightPath = self.findNodePath(node.right, path, target)

    #     if leftPath:
    #         leftPath.append(node)
    #         return leftPath
    #     if rightPath:
    #         rightPath.append(node)
    #         return rightPath

        
