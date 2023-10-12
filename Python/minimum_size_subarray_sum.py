class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        res = 0
        l = 0

        for r in range(len(nums)):
            # add right pointer to total sum
            sum += nums[r]
            while(l <= r and sum >= target):
                # check if window len is smaller than res and update
                windowLen = r - l + 1
                res = windowLen if res == 0 else min(res, windowLen)
                # remove left pointer num from sum and increment left pointer
                sum -= nums[l]
                l += 1
            
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Arrays
    # Algorithm(s): None
    # Pattern: Arrays, Sliding Window
    
    # Link: https://leetcode.com/problems/minimum-size-subarray-sum/