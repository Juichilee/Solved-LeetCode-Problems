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
    # Solve Description: First sort the nums array in ascending order. Use 3 pointers (i, l, r) for keeping track of current 
    # 3 sum being processed. For the outer loop, track index i. To prevent duplicates, check if nums[i] == nums[i-1], skipping 
    # if True. For the inner loop, implement Two Sum. Instantiate l next to i and r at the end of nums. While l < r, calculate
    # the current 3 sum, incrementing l if > 0 and decrementing r if < 0. If 3 sum == 0, add to results and update l or pointer 
    # to next non-duplicate position to keep searching. 
    ###
    
    # Link: https://leetcode.com/problems/3sum/