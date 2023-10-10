class Solution:
    def reverseWords(self, s: str) -> str:
        wordsList = []
        i = 0
        while i < len(s):
            currentWord = ""
            while i < len(s) and s[i] != " ":
                currentWord += s[i]
                i += 1
            if currentWord != "":
                wordsList.append(currentWord)
            i += 1
        
        reverseWord = wordsList[-1]
        for i in range(len(wordsList)-2, -1, -1):
            reverseWord = reverseWord + " " + wordsList[i]
        
        return reverseWord

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Arrays
    # Algorithm(s): None
    # Pattern: Arrays, String
    
    # Link: https://leetcode.com/problems/reverse-words-in-a-string/