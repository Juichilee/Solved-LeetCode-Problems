class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        idx = len(s) - 1
        count = 0
        while(idx >= 0):
            if (s[idx] != ' '):
                count += 1
            idx -= 1
            if(count > 0 and idx >= 0 and s[idx] == ' '):
                break
            
        return count

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Array
    # Algorithm(s): none
    # Pattern: Array

    ###
    # Solve Description: Start parsing string from end. Upon encountering first non-space, 
    #   increment count. If the count is greater than 0 and the next string is a space, then 
    #   stop parsing and return the count
    ###
    
    # Link: https://leetcode.com/problems/length-of-last-word/