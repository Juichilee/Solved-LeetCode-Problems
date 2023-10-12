# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head # Initialize pointers prev and curr

        while curr: 
            next = curr.next # Store current next as temp variable next
            curr.next = prev # Reverse curr next to point to prev
            prev = curr # Update prev as curr
            curr = next # Update curr to next
        return prev 
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Linked List, Iterative

    # Recursive Case
        # if not head: # base case
        #     return None
        
        # newHead = head 

        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        # return newHead
        
    # Time Complexity: O(n)
    # Space ComplexitY: O(n)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Linked List, Recursion
    
    # Link: https://leetcode.com/problems/reverse-linked-list/