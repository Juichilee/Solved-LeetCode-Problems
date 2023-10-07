class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # initiate pointers l and r

        while l < r: 
            while l < r and not self.alphaNum(s[l]): # increment l pointer, ignoring non-alphanum
                l += 1 

            while r > l and not self.alphaNum(s[r]): # decrement r pointer, ignoring non-alphanum
                r -= 1 

            if s[l].lower() != s[r].lower(): # check if l and r items are equal
                return False
            l, r = l + 1, r - 1 # update l and r by 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9')) 
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): set
    # Algorithm(s): None
    # Pattern: Two Pointers
    
    # Link: https://leetcode.com/problems/valid-palindrome/

    # Alternative Solution1: Time Complexity: O(n); Space Complexity: O(n)
        # newStr = ""

        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]

    # Alternative Solution2: Time Complexity: O(n); Space Complexity: O(n)
        # norm_str = ""
        # s = s.lower()
        # for c in s:
        #     val = ord(c)
        #     if (val >= 97 and val <= 122 or val >= 48 and val <= 57): # a - z or 0 - 9
        #         norm_str += c
        
        # reverse_norm_str = ""
        # for c in norm_str:
        #     reverse_norm_str = c + reverse_norm_str
        
        # if (norm_str == reverse_norm_str):
        #     return True
        # return False

        