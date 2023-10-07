"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None : None} # Include None edgecase

        # Pass 1: store node copies in hash map with old nodes as keys
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy 
            cur = cur.next

        # Pass 2: set parameters of copies to the copies of old node next and random params
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head] # return copy of the head for copy linked list

    # Time Complexity: O(n)
    # Space ComplexitY: O(n)
    # Datastructure(s): Linked List, Hash Table
    # Algorithm(s): None
    # Pattern: Linked List, Hash Table

    # Link: https://leetcode.com/problems/copy-list-with-random-pointer/