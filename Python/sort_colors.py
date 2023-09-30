class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, pos1, pos2):
            temp = nums[pos1]
            nums[pos1] = nums[pos2]
            nums[pos2] = temp
            
        i, l, h = 0, 0, len(nums)-1
        if len(nums) != 1:
            while i <= h:      
                if nums[i] == 0:
                    swap(nums, i, l)
                    l += 1
                if nums[i] == 2:
                    swap(nums, i, h)
                    h -= 1
                    i -= 1
                i += 1
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): 3 pointers
    # Pattern: Sorting

    ###
    # Solution Description: Instantiate three pointers: i, l, and h to be 0, 0, and len(nums)-1. i keeps 
    #   track of the current color being processed. l and h are updated such that everything to the left 
    #   of l is '0' while everything to the right of h is '2'. While pointer i is less than equal to h, 
    #   check if the current num at i is '0'. If it is, then swap with the number at pointer l and increment
    #   l. However, if it is equal to '2', swap with the number at pointer h and increment h. Increment
    #   pointer i to the next position and repeat. 
    ###
    
    # Link: https://leetcode.com/problems/sort-colors/