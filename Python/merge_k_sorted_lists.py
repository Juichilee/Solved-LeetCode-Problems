# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edgecase: check for empty lists
        if not lists or len(lists) == 0:
            return None
        
        # Merge
        while len(lists) > 1:
            mergedLists = []

            # Merge every two consective list
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Edgecase: 2 index should be less than len(lists)
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Append result of l1 l2 merge into mergedLists for future merges
                mergedLists.append(self.mergeList(l1, l2))
            # Update lists with mergedLists
            lists = mergedLists

        return lists[0]
    
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next

    # Time Complexity: O(nlog(k))
    # Space ComplexitY: O(1)
    # Datastructure(s): Linked List
    # Algorithm(s): None
    # Pattern: Merging
    
    ###
    # Solve Description: Follows from merge_two_sorted_lists problem. Start with a list that stores
    #   all of the sorted linked lists. Then, while the list has more than one element, separate each
    #   linked list into groups of 2, merge them, and store them in a new list. Return the remaining
    #   sorted linked list.
    ###
    
    # Link: https://leetcode.com/problems/merge-k-sorted-lists/