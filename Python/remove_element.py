class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Array
    # Algorithm(s): none
    # Pattern: Array
    
    ###
    # Solve Description: Use a pointer k to indicate the position to write to when nums[i] != val. 
    #   Loop through each num in nums and check if the current num is equal to val. If not equal, 
    #   then replace the num at index k with the current num and increment k to the next pos. 
    ###
    
    # Link: https://leetcode.com/problems/remove-element/