class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        
        # Take into account [1] edge case
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # Check if mid is in left or right sorted position
            # left sorted position
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            # right sorted position
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1

    # Time Complexity: O(log(n))
    # Space ComplexitY: O(1)
    # Datastructure(s): None
    # Algorithm(s): Binary Search
    # Pattern: Binary Search

    ###
    # Solve Description: Instantiate a left and right pointer positioned at either end of nums. 
    #   perform binary search on the list, however, after calculating the midpoint value,
    #   check if it lies within the left sorted position or right sorted position. Then, 
    #   compare the value of the target with the midpoint value and assign the left or right
    #   pointers to their new position.  
    ###
    
    # Link: https://leetcode.com/problems/search-in-rotated-sorted-array/