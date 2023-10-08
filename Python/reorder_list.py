# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Splitting linked list into 2 pieces: regular and reversed. Prev is initialized as end of reversed list and slow.next is end of regular list
        second = slow.next
        prev = slow.next = None 
        
        while second:
            # Use temporary var to store next node in reverse array
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

    # Time Complexity: O(n)
    # Space ComplexitY: O(1)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Linked List
    
    # Link: https://leetcode.com/problems/reorder-list/







