class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if it is the start of a sequence
            if (n - 1) not in numSet: # check if n is start of a sequence
                length = 0
                while (n + length) in numSet: # count consecutive numbers in set
                    length += 1
                longest = max(length, longest) # update longest

        return longest
        
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): set
    # Algorithm(s): None
    # Pattern: Arrays & Hashing

    # Link: https://leetcode.com/problems/longest-consecutive-sequence/