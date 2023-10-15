class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter one line solution: return Counter(s) == Counter(t)
        # Sorted one line solution: return sorted(s) == sorted(t)

        if len(s) != len(t): # Check if either strings are same length
            return False

        countS, countT = {}, {} # letter : count

        for i in range(len(s)): # add counts up for each letter
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS: # check each letter key in countS, see if same in count in countT
            if countS[c] != countT.get(c, 0):
                return False
        return True

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): hash table
    # Algorithm(s): None
    # Pattern: Arrays & Hashing
    
    # Link: https://leetcode.com/problems/valid-anagram/