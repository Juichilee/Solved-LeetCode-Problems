class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # skip current i pointer if already processed before to avoid duplicates
            if i > 0 and a  == nums[i-1]: 
                continue
            
            # two_sum problem incorporating pointer i
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # continue searching for matches. Can update starting from 
                    # either l or r pointer
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # Datastructure(s): set
    # Algorithm(s): sort() (preferably O(nlog(n))
    # Pattern: Three Pointers (i, l, r)
                    
    ###
    # Solve Description: First sort the nums array in ascending order. 
    ###
    
    # Link: https://leetcode.com/problems/3sum/