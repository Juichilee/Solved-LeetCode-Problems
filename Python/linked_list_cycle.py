# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    # Time Complexity: O(n)
    # Space ComplexitY: O(1)
    # Datastructure(s): Linked List
    # Algorithm(s): Fast and Slow Pointer (Floyd Tortoise and Hare)
    # Pattern: Fast and Slow Pointer

    # Link: https://leetcode.com/problems/linked-list-cycle/