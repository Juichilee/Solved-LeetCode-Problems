class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE
        # res = 0

        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)

        # return res

        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r]) # calculate area
            res = max(res, area) # store bigger area

            if height[l] < height[r]:
                l += 1
            else:   # if height[l] > height[r] or if height[l] == height[r]
                r -= 1
        
        return res 

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): None
    # Algorithm(s): None
    # Pattern: Two pointers
    
    ###
    # Solve Description: Instantiate 2 pointers, positioned at both ends of the height array. 
    #   While the left pointer is less than the right pointer, calculate the area between the current
    #   left and right pointers. Update the max area in res if applicable. Then, if the height at the 
    #   left pointer is larger than the height at the right, increment the left pointer. Otherwise, decrement
    #   the right pointer.
    ###
    
    # Link: https://leetcode.com/problems/container-with-most-water/