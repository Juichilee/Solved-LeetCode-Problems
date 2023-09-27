from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)  # or float("inf")
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Hashtable
    # Algorithm(s): None
    # Pattern: None

### 
# Solution Description: Use Python Counter function to turn text and "balloon"
#   into dictionaries where the key are the letters and the values are the letter counts.
#   Then, go through each key letter and find the minimum value between the current results
#   and the wordCount ratio between text and "balloon", updating the res each time. 
###

# Link: https://leetcode.com/problems/maximum-number-of-balloons/