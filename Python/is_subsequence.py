class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sPointer = 0
        for charT in t:
            if (sPointer < len(s) and charT == s[sPointer]):
                sPointer += 1
        
        return True if sPointer == len(s) else False

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Stack
    # Algorithm(s): none
    # Pattern: Array

    ###
    # Solve Description: Use a pointer for s to keep track of current char being compared. 
    #   Go through each char in t and compare with char at s pointer, incrementing s pointer 
    #   if they match. If sPointer matches len(s), s is a subsequence of t
    ###
    
    # Link: https://leetcode.com/problems/is-subsequence/