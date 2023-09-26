class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # edge case if only 1 element in nums
        if len(nums) == 1:
            return 0

        right_sum = sum(nums[1:])
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            if i + 1 < len(nums): # check to see if i+1 is a valid pos in nums
                right_sum -= nums[i+1]           

        return -1

    # Time Complexity: O(n)
    # Space ComplexitY: O(1)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Array
    
    ###
    # Solve Description: Instantiate two variables for holding left and right sums. Since the pivot
    #   starts at 0, the right sum is the sum of everything but the 0th element. The left sum is 0
    #   because it is to the left of the 0th element pivot. Then, when looping through each possible
    #   pivot indices, add the previous pivot element to left_sum and subtract the next pivot element
    #   from right_sum. When the two sums match, return the current pivot index. Otherwise, if the
    #   loop completes, return -1.
    
    # Link: https://leetcode.com/problems/find-pivot-index/