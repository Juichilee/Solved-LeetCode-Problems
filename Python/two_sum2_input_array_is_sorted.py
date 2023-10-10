class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l <= r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l += 1
            elif sum > target:
                r -= 1

    # Time Complexity: O(n) 
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Two pointer

    ###
    # Solve Description: Initialize l and r pointers at beginning and end of numbers. 
    #   If the current sum is equal to the target, return l and r pointers and indices. 
    #   If the sum is less than the target, increment the left pointer. If the sum is 
    #   greater than the target, increment the right pointer
    ###
    
    # Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/