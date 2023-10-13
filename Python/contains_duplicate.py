class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set() # Create hashset to store unique num
        for n in nums:
            if n in hashset: # Check if current num is in hashset
                return True
            hashset.add(n) # if not in hashset, add to hashset
        return False

        # Alternative Solution: 
        # for i in range(len(nums)-1):
        #     j = i
        #     while (j >= 0) and (nums[j] < nums[j+1]):
        #         temp = nums[j]
        #         nums[j] = nums[j+1]
        #         nums[j+1] = temp
        #         j = j-1

        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): set
    # Algorithm(s): None
    # Pattern: Arrays & Hashing
    
    # Link: https://leetcode.com/problems/contains-duplicate/