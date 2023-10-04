# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Initialize results array and queue for BFS. Add root to queue
        res = []
        q = collections.deque()
        q.append(root)

        # While the queue is not empty...
        while q:
            qLen = len(q)
            level = []
            # Iterate through current queue...
            for i in range(qLen):
                # Pop current node from queue. If node is not null, add node to current level list and append node children to queue
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # Edgecase: If level is not empty, add level to results array
            if level:
                res.append(level)
        
        return res
                

    # Time Complexity: O(n)
    # Space ComplexitY: O(n)
    # Datastructure(s): Tree
    # Algorithm(s): BFS
    # Pattern: None

    ###
    # Solve Description: Use BFS traversal. Implement BFS using a dequeue.
    #   For each depth, pop the stored node from one end of the dequeue, retrieve
    #   the node's children, and append the children to the other end of the dequeue.
    #   While appending the children nodes to the dequeue, append them to a temporary 
    #   list 'level' to keep track of nodes in the level. If level is non-empty, then
    #   append to results list.
    ###
    
    # Link: https://leetcode.com/problems/binary-tree-level-order-traversal/