class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): set
    # Algorithm(s): None
    # Pattern: Sliding Window

    ### 
    # Solve Description: Initialize a left and right pointer and a char set. 
    #   As the right pointer moves across the string, check if the letter at 
    #   right pointer already exists in the set. If it does, remove letters from 
    #   the set starting from the left pointer until the set is unique again. Add 
    #   right pointer letter to the set and update res if length between left and right pointer (r - 1 + 1) is greater
    ###
    
    # Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/