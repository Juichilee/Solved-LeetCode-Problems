class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = collections.defaultdict(set) # hashset for checking cols
        rows = collections.defaultdict(set) # hashset for checking rows
        squares = collections.defaultdict(set) # key = (r/3, c/3). /3 maps r, c to one of the sudoku matrices

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # ignore cells with "."
                    continue
                # return False if any of these conditions are true
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                # update all hashsets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
    # Time Complexity: O(9^2)
    # Space Complexity: O(9^2)
    # Datastructure(s): HashSet
    # Algorithm(s): None
    # Pattern: Arrays, Matrices, HashSet
    
    ###
    # Solution Description: Initialize col and row dictionaries that store sets that check the validity
    #   of each row and col. Initialize a squares dictionary that also stores sets checking the validity
    #   of each 3x3 matrix on the board. Go through each cell in the sudoku board, ignoring empty cells.
    #   If the current cell value is in rows dictionary set, the cols dictionary set, or in the squares 
    #   dictionary set, return False. Otherwise, update all of the dictionary sets with the cell value.
    ###

    # Link: https://leetcode.com/problems/valid-sudoku/