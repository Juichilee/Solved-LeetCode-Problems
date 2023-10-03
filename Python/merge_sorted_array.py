class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        # for example: nums1[1, 2, 3, 0, 0, 0] nums2[4, 5, 6]
        # indices:                 i        k              j

        # As long as i and j are greater than or equal to 0...
        while(i >= 0 and j >= 0):
            if(nums1[i] > nums2[j]): # if num @ i > num @ j, swap with placeholder '0' @ k
                nums1[k] = nums1[i]
                nums1[i] = 0
                # decrement both k and i to next pos
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j] # else if num @ j >= num @ i, swap with placeholder '0' @ k
                nums2[j] = 0
                # decrement both k and j to next pos
                k -= 1
                j -= 1
        # special case: if i is negative, fill in placeholder '0's from the start of nums 1 with nums2
        if i < 0:
            for s in range(j+1):
                nums1[s] = nums2[s]
        
        return nums1

    # Time Complexity: O(m + n)
    # Space ComplexitY: O(1)
    # Datastructure(s): Arrays
    # Algorithm(s): None
    # Pattern: Arrays, Two pointer/Three pointer
    
    ###
    # Solve Description: Initialize 3 pointers i, j, and k. i points to end of
    #   list nums1 before the zeros, j points to end of nums2, and k points to end
    #   of list nums1 after the zeros. As long as i and j are gte zero, compare the nums
    #   at nums[i] and nums2[j]. If the former is greater, then store nums1[i] into the
    #   open position at nums1[k]. Otherwise, store nums2[j] into nums1[k]. Decrement 
    #   both k and j to the next position. If nums1 ends up having placeholder zeros
    #   at the start and all of the original nums1 elements have already been placed,
    #   then copy the remainder of nums2 to fill up all the placeholder zeros at the start.
    ###
    
    # Link: https://leetcode.com/problems/merge-sorted-array/