class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        # initailize rows, cols, visited set and num_islands
        rows, cols = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def bfs(r, c):
            q = collections.deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q.append([r, c])
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                # check for adjacent islands in each direction
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # if new r and c are in matrix range, is an island, and has not been visited...
                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c) not in visited):
                        # add r, c coordinates to queue and visited set
                        q.append([r, c])
                        visited.add((r, c))

        # go through each row and col in matrix
        for r in range(rows):
            for c in range(cols):
                # if current row and column is an island and not in visited...
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_islands += 1
                    bfs(r, c) # bfs for checking for adjacent islands and updating visited
        
        return num_islands

    # Time Complexity: O(m x n)
    # Space Complexity: O(m + n)
    # Datastructure(s): Set, Queue
    # Algorithm(s): BFS
    # Pattern: Graph, BFS, Set, Union Find
    
    # Link: https://leetcode.com/problems/number-of-islands/