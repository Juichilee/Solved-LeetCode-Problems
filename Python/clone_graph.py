"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        oldToNew = {}

        def dfs(node):
            
            if node in oldToNew:
                return oldToNew[node]
            
            newNode = Node(node.val)
            oldToNew[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))

            return newNode

        return dfs(node) if node else None

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): HashTable
    # Algorithm(s): DFS
    # Pattern: Graph, DFS, HashTable

    # Link: https://leetcode.com/problems/clone-graph/