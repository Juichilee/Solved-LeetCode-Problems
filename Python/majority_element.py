class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityCount = len(nums)//2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > majorityCount:
                return num

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Array, Hashtable
    # Algorithm(s): None
    # Pattern: Array, Hashtable
    
    # Link: https://leetcode.com/problems/majority-element/