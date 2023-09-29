class Solution:
    def climbStairs(self, n: int) -> int:
        # DP bottom up approach
        # Subproblems dependency start from base case
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): Bottom-up DP
    # Pattern: None

    ###
    # Solve Description: Check edgecase if n <= 3, in which case, there are n distinct ways. 
    #   The problem takes a bottom-up approach where the solution to calculating n steps 
    #   can be broken up into subproblems adding the previous n-1, n-2 solutions together.
    #   Ex: distinct(n=4) = distinct(n=3) + distinct(n=2). 
    ###
    
    # Link: https://leetcode.com/problems/climbing-stairs/