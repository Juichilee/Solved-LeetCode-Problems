class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]
        l, r = 0 , len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]: # If left integer is less than right integer (already sorted, so update res and break)
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2 # Calculate mid index using integer division
            res = min(res, nums[m]) # Update res if num at mid index is less than res
            if nums[m] >= nums[l]: # Move left or right pointer to +- m
                l = m + 1
            else:
                r = m - 1
        
        return res
        
    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    # Datastructure(s): array
    # Algorithm(s): None
    # Pattern: Binary Search
 
    # Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/