class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # go from the ocean to the cells

        pac, atl = set(), set() # (r, c)
        ROW, COL = len(heights), len(heights[0])

        # BFS for visiting each reachable node
        def dfs(r, c, visit, previousHeight):
            # if current coordinates have already been visited, are not within the matrix, or is less than previously visited node's height, we skip entirely
            if((r, c) in visit or 
                r < 0 or c < 0 or r == ROW or c == COL or
                heights[r][c] < previousHeight):
                return
            # add current coordinates to visit set
            visit.add((r, c))
            # begin bfs for all adjacent coordinates
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # calculate the nodes that can be reached starting from top and bottom
        for c in range(COL):
            dfs(0, c, pac, heights[0][c]) # starting nodes for top (pacific ocean)
            dfs(ROW - 1, c, atl, heights[ROW - 1][c]) # starting nodes for bottom (atlantic ocean)
        # calculate the nodes that can be reached starting from left and right
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0]) # starting nodes for left (pacific ocean)
            dfs(r, COL - 1, atl, heights[r][COL - 1]) # starting nodes for right (atlantic ocean)
        
        res = []
        # brute force calculate which nodes are in both pac and atl
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res

    # Time Complexity: O(m x n)
    # Space Complexity: O(m x n)
    # Datastructure(s): Set
    # Algorithm(s): DFS
    # Pattern: Graph, DFS, Set
    
    # Link: https://leetcode.com/problems/pacific-atlantic-water-flow/