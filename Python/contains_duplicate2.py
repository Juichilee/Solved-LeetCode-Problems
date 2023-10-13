class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        
        duplicatesTable = {}
        j = 0
        for i in range(len(nums)):
            priorIndex = duplicatesTable.get(nums[i], None)
            if priorIndex == None:
                duplicatesTable[nums[i]] = i
            else:
                diff = abs(i - priorIndex)
                if diff <= k:
                    return True
                duplicatesTable[nums[i]] = i

        return False

    # Time Complexity: O(n)
    # Space ComplexitY: O(n)
    # Datastructure(s): Arrays
    # Algorithm(s): None
    # Pattern: Arrays, HashTable
    
    # Link: https://leetcode.com/problems/contains-duplicate-ii/