class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapST, mapTS = {}, {} # map strings from S and T to each other

        for c1, c2 in zip(s, t): # zip places char from 2 strings in the same arr
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Array, Hashtable
    # Algorithm(s): None
    # Pattern: Array, Hashtable, Mapping
        
    # Link: https://leetcode.com/problems/isomorphic-strings/