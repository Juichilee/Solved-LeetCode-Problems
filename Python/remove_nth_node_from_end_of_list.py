# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Shift right by n
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Keep shifting right and left until right is null
        while right:
            left = left.next
            right = right.next
        
        # Delete node at left.next by skipping it
        left.next = left.next.next

        # Return head through dummy.next
        return dummy.next

    # Time Complexity: O(n)
    # Space ComplexitY: O(1)
    # Datastructure(s): Linked List
    # Algorithm(s): None
    # Pattern: Linked List

    ###
    # Solve Description: Initialize a dummy node pointing to head. Set left pointer to dummy and right pointer to head.
    #   The idea is to separate left and right by n and maintain the distance while shifting left and right pointers 
    #   until the end of the list is reached. Then, the left pointer should automatically be positioned at the node
    #   before the desired node to remove. Then, you would delete the nth node from the end by skipping it through
    #   setting left.next = left.next.next
    ###
    
    # Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/