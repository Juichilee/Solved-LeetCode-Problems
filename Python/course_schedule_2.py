class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Teaches topological sort
        # build adjacency list of prereq
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output

    # Time Complexity: O(p + n) p, n = prereq(edge), node
    # Space Complexity: O(n)
    # Datastructure(s): HashSet, Array
    # Algorithm(s): DFS, Topological Sort
    # Pattern: Graph, DFS

    # Link: https://leetcode.com/problems/course-schedule-ii/