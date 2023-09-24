# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() 
        cur = dummy

        carry = 0 # stores the carry term of sums greater than 9
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10 # calculate the next carry
            val = val % 10 # get the remainder of val without carry
            cur.next = ListNode(val) 

            # update cur and l1, l2 ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Linked List
    # Algorithm(s): None
    # Pattern: Mathematics

    ###
    # Solve Description: Create a dummy node to hold the return value. As long as l1 or l2 have not reached 
    #   the end or the carry is non-zero, calculate the sum of the current l1 and l2 node values. Make sure the
    #   carry value is factored into the current sum and calculated for the next set of nodes. Update the nodes
    #   to point to the next position if it exists.
    ###
    
    # Link: https://leetcode.com/problems/add-two-numbers/description/