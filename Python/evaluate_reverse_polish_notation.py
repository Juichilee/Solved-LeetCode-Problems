class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        numStack = []
        
        # helper function for performing operation
        def performOperation(left, right, op):
            if ord(op) == ord("+"):
                return (left + right)
            if ord(op) == ord("-"):
                return (left - right)
            if ord(op) == ord("*"):
                return (left * right)
            if ord(op) == ord("/"):
                val = (left / right)
                if val > 0:
                    return floor(val)
                return ceil(val)

        for token in tokens:
            # check if token is a num or op
            if ((len(token) == 1) and (ord(token) == ord("+") or 
                ord(token) == ord("-") or 
                ord(token) == ord("*") or 
                ord(token) == ord("/"))):
                # print("numStack: ", numStack)
                right = numStack.pop()
                left = numStack.pop()
                res = performOperation(left, right, token)
                # print("op: ", token)
                # print("res: ", res)
                numStack.append(res)
            else:
                numStack.append(int(token)) # append tokens that are integers to numStack

        return numStack[0] # last elem in numStack should be results

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Stack
    # Algorithm(s): none
    # Pattern: Stack

    ###
    # Solve Description: For each token, check if token is a num or op. If it is a num, 
    #   just append to num Stack as an integer. If it is an op, pop two times from num stack, 
    #   with the first being right operand and the second the left. Then, perform the operation 
    #   specified by the operand and store the return value
    ###
    
    # Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/