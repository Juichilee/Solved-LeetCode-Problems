class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # using output array to store forward and backward pass results. default value is 1

        prefix = 1 # default prefix (left of idx 0) is 1
        for i in range(len(nums)): # forward pass
            res[i] = prefix # store current prefix in non-prefix-suffix position
            prefix *= nums[i] # update prefix for next pos by multiplying it by non-prefix-suffix
        
        postfix = 1 # default suffix (right of len(nums)-1) is 1
        for i in range (len(nums) - 1, -1, -1): # backward pass
            res[i] *= postfix # multiply current prefix by current postfix. calculates product of array without pos i
            postfix *= nums[i] # update postfix for next pos by multiplying nums[i]

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1) (not counting output array)
    # Datastructure(s): array
    # Algorithm(s): None
    # Pattern: Arrays & Hashing
    
    # Link: https://leetcode.com/problems/product-of-array-except-self/