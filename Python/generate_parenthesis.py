class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = set()
        res = []
        stack = []
        
        # function for checking if stack is in valid combo
        def checkValid(stack):
            tempStack = []
            if stack[0] == ")" or stack[-1] == "(":
                return False
            for bracket in stack:
                if bracket == "(":
                    tempStack.append("(")
                if tempStack and bracket == ")":
                    tempStack.pop()
            return False if tempStack else True

        def dfs(stack, numStart, numClose):
            # if all parenthesis have been used
            if numStart == 0 and numClose == 0:
                combo = ""
                for bracket in stack:
                    combo += bracket
                if (combo not in combinations and checkValid(stack)):
                    # check if in combinations set already
                    combinations.add(combo)
                    res.append(combo)

            # allow traversal as long as brackets available
            if (numStart > 0):
                stack.append("(")
                dfs(stack, numStart - 1, numClose)

            if (numClose > 0):
                stack.append(")")
                dfs(stack, numStart, numClose - 1)
            
            # remove previously added brace from stack when moving back up a level
            if stack:
                stack.pop()
            return

        dfs(stack, n, n)
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Stack, HashSet
    # Algorithm(s): DFS
    # Pattern: DFS, Stack

    # Solve Description: Use a set to keep track of all combinations. Initialize a counter for number 
    #   of starting and closing braces. When traversing a potential combination, add a brace to the 
    #   stack and decrement the number of the brace used when calling recursively. If the max number of 
    #   braces are used, then loop through stack. If the combination stored by the stack is valid and not 
    #   in the combinations set, add to the combinations set and results
    ###
    
    # Link: https://leetcode.com/problems/generate-parentheses/description/
