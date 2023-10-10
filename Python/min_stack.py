class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

    # Time Complexity: O(1)
    # Space Complexity: O(n)
    # Datastructure(s): Stack
    # Algorithm(s): None
    # Pattern: Stack

    # Solve Description: Create a regular stack to hold values and a minStack to keep track of the minimum at all the points in the stack. 
    
    # Link: https://leetcode.com/problems/min-stack/