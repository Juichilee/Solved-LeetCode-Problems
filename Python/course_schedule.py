class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preq = {i : [] for i in range(numCourses)} # [cr: [preq]]
        for cr, pr in prerequisites:
            preq[cr].append(pr)
        
        visited = set() # keeps track of visited courses during DFS

        # DFS
        def dfs(cr):
            # base cases for recursion
            if cr in visited: # if current cr has already been visited, a loop exists
                return False
            
            if preq[cr] == []: # if current cr has no preq, then return True
                return True
            
            visited.add(cr) # otherwise, add cr to visited set for later

            # continue DFS on cr's prequisites, checking for False returns
            for pr in preq[cr]:
                if not dfs(pr): return False
            
            visited.remove(cr) # remove cr from visited before returning to prior course
            preq[cr] = [] # set cr's prequisites to [] to indicate cr can be completed
            return True

        # DFS for each course to make sure non-connected courses aren't missed
        for cr in range(numCourses):
            if not dfs(cr): return False
        
        return True

    # Time Complexity: O(n + p)
    # Space Complexity: O(n)
    # Datastructure(s): Set, Hashtable
    # Algorithm(s): DFS
    # Pattern: Graph, DFS, Set, Hashtable

    # Link: https://leetcode.com/problems/course-schedule/