class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letterToWord = {}
        usedWordSet = set()
        stringArr = s.split(" ")

        # Edge case if stringArr and pattern lens are not equal
        if len(stringArr) != len(pattern):
            return False

        for i in range(len(pattern)):
            word = letterToWord.get(pattern[i], -1)
            if word == -1 and stringArr[i] not in usedWordSet:
                letterToWord[pattern[i]] = stringArr[i]
                usedWordSet.add(stringArr[i])
                continue
            if word != stringArr[i]:
                return False
        return True

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Hashtable, Set
    # Algorithm(s): None
    # Pattern: None
    
    ###
    # Solve Description: Instantiate a hashtable for mapping letter to word and a set for keeping track
    #   of words that have been stored into the table. Loop through each char in the pattern, mapping 
    #   the corresponding word in the same position to the char if it doesn't exist in the table AND if
    #   the word has not been mapped before (each word can only be mapped once). If the current char has
    #   a word it maps to, check if the retrieved word is the same as the string in the current pattern 
    #   to word position. Return False if they do not match. Otherwise, if the whole loop completes, 
    #   return True
    ###
    
    # Link: https://leetcode.com/problems/word-pattern/

        
