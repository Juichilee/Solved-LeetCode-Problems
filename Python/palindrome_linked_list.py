# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        # fast and slow pointers to get middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half of linked list starting from slow pointer
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # compare reversed second half with the first half of linked list
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Linked List
    # Algorithm(s): none
    # Pattern: Fast and Slow Pointers
    
    # Link: https://leetcode.com/problems/palindrome-linked-list/