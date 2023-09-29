class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot: # BS across vertical axis for target row
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot): # if did not find target row, return False
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r: # BS across horizontal axis for target
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

    # Time Complexity: O(log(m * n)) 
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): Binary Search
    # Pattern: Binary Search

    # Solve Description: First, perform BS on vertical axis to find target row, 
    #   assigning new top, bot pointers by checking if the target is > or < the
    #   endpoints of the midpoint row. If target row cannot be found (i.e., the top and bottom pointers overlap), 
    #   return False. Else, perform BS on the target row, returning True if target 
    #   matches the midpoint, otherwise, if the left and right pointer overlap, return False  

    # Link: https://leetcode.com/problems/search-a-2d-matrix/