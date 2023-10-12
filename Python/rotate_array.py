class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            val = nums.pop()
            nums.insert(0, val)
            k -= 1

    # Time Complexity: O(n)
    # Space ComplexitY: O(1)
    # Datastructure(s): Arrays
    # Algorithm(s): None
    # Pattern: Arrays
    
    # Link: https://leetcode.com/problems/rotate-array/