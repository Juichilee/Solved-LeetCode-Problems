class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]" : "[", "}": "{"}

        for c in s:
            if c in closeToOpen: # Check if char is closing bracket in closeToOpen, only appending open brackets to stack
                if stack and stack[-1] == closeToOpen[c]: # stack is not empty and first element in stack is matching opening bracket, remove first element and continue
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False # Only return True if stack is empty, otherwise return False

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Datastructure(s): stack, hash table
        # Algorithm(s): none
        # Pattern: stack

        # Alternative Solution
        # if len(s) < 2:
        #     return False

        # stack = []
        # brackets = ['()', '[]', "{}"]
        # open_brackets = ['(', '[', '{']
        # for bracket in s:
        #     if (bracket in open_brackets):
        #         stack.append(bracket)
        #     else:
        #         if (len(stack) == 0):
        #             return False
        #         open_bracket = stack.pop()
        #         bracket = open_bracket + bracket
        #         if not bracket in brackets:
        #             return False
        
        # if len(stack) != 0:
        #     return False
        # return True
                
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Datastructure(s): stack
        # Algorithm(s): none
        # Pattern: stack
    
        ###
        # Solve Description: Use a stack to keep track of the current latest opening brace. If the current char is
        #   an opening brace, add it to the stack. If the current char is a closing brace, check if it matches the 
        #   latest opening brace stored in the stack. If they match, remove the latest brace from the stack, otherwise,
        #   return False.
        ###
        
        # Link: https://leetcode.com/problems/valid-parentheses/