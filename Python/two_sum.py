class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {} # val : index

        for i, n in enumerate(nums): 
            diff = target - n # find the necessary val to add up to target as diff

            # Check if diff exists in prevMap values
            diff_idx = prevMap.get(diff, -1)
            if(diff_idx != -1):
                return [i, diff_idx]
                
            prevMap[n] = i # otherwise, update prevMap with current num index and val
            
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): hash table
    # Algorithm(s): None
    # Pattern: Arrays & Hashing

    ###
    # Solve Description: Use a HashMap mapping the differences between each num and the 
    #   target to the num's index for easy lookup. Iterate through each num and check if 
    #   the current num difference exists in the HashMap. Return if it exists, otherwise, update HashMap
    ###
    
    # Link: https://leetcode.com/problems/two-sum/description/


            


