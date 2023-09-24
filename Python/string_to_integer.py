class Solution:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            # state == 0: Handles empty spaces. Transitions to state 1 if current char is a sign, state2 if current char is digit
            if state == 0: 
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            # state == 1: Handles edge case if there are no digits after sign
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            # state == 2: Main handler for reading characters as integers. Breaks loop upon reading non-integer
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        # Add sign to value and clamp between (2^31)-1 and -2^31
        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value

                
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): Deterministic Finite Automaton (DFA)
    # Pattern: String

    ###
    # Solution from: "Fast and simpler DFA approach (Python 3)" (spencerwoo)
    ###
    
    # Link: https://leetcode.com/problems/string-to-integer-atoi/