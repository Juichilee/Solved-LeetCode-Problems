# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node (tail) to store node results
        dummy = ListNode() 
        tail = dummy

        # while list1 and list2 are not null
        while list1 and list2: 
            # Compare list1 and list2 val, setting tail.next to whichever is smaller and updating the smaller list to its next node
            if list1.val < list2.val: 
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Update tail to next node by default
            tail = tail.next

        # Set tail.next to the remainder of non-null list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

    # Time Complexity: O(n)
    # Space ComplexitY: O(1)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Linked List

    ###
    # Solve Description: Instantiate a dummy pointer to point to result head and tail pointer to point to result tail. 
    #   While list1 and list2 pointers are not null, compare both list1 and list2 values, setting tail.next to whichever
    #   is smaller and updating the pointer to the next position. If list1 or list2 still have values left, append the 
    #   remainder to tail.next. Return the results through dummy.next.  
    ###
    
    # Link: https://leetcode.com/problems/merge-two-sorted-lists/
                
            
                

                