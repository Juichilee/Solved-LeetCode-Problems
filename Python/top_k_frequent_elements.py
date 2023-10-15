class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # num : count
        freq = [[] for i in range(len(nums) + 1)] # bucket sort. idx = count, vals = nums with that count

        for num in nums: # Store each number and their counts into count dict
            count[num] = count.get(num, 0) + 1
        
        for n, c in count.items(): # bucket nums with the same count in freq
            freq[c].append(n) # i.e. {1 : 2, 2 : 2} -> freq[2] = [1, 2]

        res = []

        for i in range(len(freq) - 1, 0, -1): # navigate freq array backwards 
            for n in freq[i]: # skips if freq[i] = []
                res.append(n) # append all nums within bucket to res
                if len(res) == k: # if len(res) is same as k, return
                    return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): hashtable, 2D array, array
    # Algorithm(s): None
    # Pattern: Arrays & Hashing
    
    # Link: https://leetcode.com/problems/top-k-frequent-elements/