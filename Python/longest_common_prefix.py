class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        for i in range(len(strs)):
            if i == 0:
                commonPrefix = strs[i]
                continue
            
            j = 0

            while (j < len(commonPrefix) and j < len(strs[i]) and commonPrefix[j] == strs[i][j]):
                j += 1

            if (j == 0):
                return ""

            commonPrefix = commonPrefix[0:j]
        
        return commonPrefix

    # Time Complexity: O(n * m) n, m = number of strings, number of chars in string
    # Space Complexity: O(1)
    # Datastructure(s): Array
    # Algorithm(s): none
    # Pattern: Array

    ###
    # Solve Description: Use first string as the commonPrefix. For each new string, 
    #   compare both of their letters at the same index and increment j if they match. 
    #   At the end, set the new commonPrefix to span 0 to j
    ###
    
    # Link: https://leetcode.com/problems/longest-common-prefix/