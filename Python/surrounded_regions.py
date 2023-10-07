class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        notSurrounded = set() # (i, j)
        m, n = len(board), len(board[0])

        def dfs(i, j):

            if (i < 0 or i >= m or
                j < 0 or j >= n or
                board[i][j] == "X" or (i, j) in notSurrounded):
                return 
            
            notSurrounded.add((i, j))

            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for nr, nc in dirs:
                ni, nj = i + nr, j + nc
                dfs(ni, nj)
            return

        # dfs starting m, n = 0 - m-1, 0
        for i in range(m):
            dfs(i, 0)
        # dfs starting m, n = 0 - m-1, n-1
        for i in range(m):
            dfs(i, n-1)
        # dfs starting m, n = 0, 0 - n-1
        for j in range(n):
            dfs(0, j)
        # dfs starting m, n = m-1, 0 - n-1
        for j in range(n):
            dfs(m-1, j)

        # replace all cells that are not in the notSurrounded set
        for i in range(m):
            for j in range(n):
                if (i, j) not in notSurrounded:
                    board[i][j] = "X"

    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)
    # Datastructure(s): HashSet
    # Algorithm(s): DFS
    # Pattern: Graph, DFS, HashSet

    # Link: https://leetcode.com/problems/surrounded-regions/