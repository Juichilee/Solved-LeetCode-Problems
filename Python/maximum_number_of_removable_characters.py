class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        # helper for returning string without chars from removable[0: idx] 
        def removeChar(s, idx):
            removeSet = set(removable[:idx+1])
            newS = ""
            for j in range(len(s)):
                if not j in removeSet:
                    newS += s[j]
            return newS

        # helper for checking if the subsequence of a string is still valid
        def checkSubSequence(s, p):
            match = 0
            for c in s:
                if c == p[match]:
                    match += 1
                if match == len(p):
                    return True
            return False
        
        # Binary Search on removable to find suitable k
        l, r = 0, len(removable)-1
        k = 0
        while (l <= r):
            m = (l + r)//2
            newS = removeChar(s, m)
            # if checkSubsequence is good, update left pointer
            if checkSubSequence(newS, p): 
                k = m + 1 # since m is 0-indexed, we add 1 to obtain k-elements
                l = m + 1
            else:
                r = m - 1

        return k

    # Time Complexity: O(n*log(n))
    # Space Complexity: O(n)
    # Datastructure(s): Array
    # Algorithm(s): Binary Search
    # Pattern: Arrays
    
    ###
    # Solve Description: Use Binary Search on removable array, removing chars from 
    #   string s until the current midpoint in removable array. Then, check if p
    #   is still a valid subsequence of the new string. If it is, then update k
    #   to be midpoint m + 1 and set l to also be m + 1 to continue search in 
    #   removable array right half. Otherwise, set r to m - 1 to continue search
    #   in left half.
    ###
    
    # Link: https://leetcode.com/problems/maximum-number-of-removable-characters/

