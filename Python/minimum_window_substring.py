class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return "" # Edge case t is empty string

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [ -1, -1], inf
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r+1] if resLen != inf else ""

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): hash table, array
    # Algorithm(s): none
    # Pattern: Sliding Window

    ###
    # Solution Description: Initialize two dicts, countT and window. countT tracks the count for each char in string t
    #   while window tracks the count for each char in the current string s window. Then, initialize two variables,
    #   have and need, that track the current satisfied amount of char and the total chars required for the window
    #   to be a substring. For keeping track of the current string window, use two pointers l and r. While incrementing
    #   the r pointer, update the window amount for the current char. If the character is part of the required chars in
    #   countT and count amount of that character in windows and countT are equal, updated the "have" variable. If the "have"
    #   equals the "need", then, update the results if the current window length is smaller than previous window lengths.
    #   Then, update the pointer l and the count of the corresponding char at that position for window. If the removed char
    #   was a required char and it causes its count in window to fall below its required count in countT, decrement have. 
    ###
    
    # Link: https://leetcode.com/problems/minimum-window-substring/description/
