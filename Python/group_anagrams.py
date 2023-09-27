class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # count dict : string anagrams. defaultdict generates list if key does not exist yet
        
        for s in strs: # for each string in strs array
            count = [0] * 26 # instantiate count array where a ... z is represented by index

            for c in s: # for each char in current string
                count[ord(c) - ord("a")] += 1 # char unicode value : count
            
            res[tuple(count)].append(s) # tuple is immutable so it can be a key.
            # e.g. 'eat' => [e: 1, a: 1, t:1] <== 'tea'

        return res.values()

    # Time Complexity: O(m * n) (m is avg len of s i nstrs, n is len(strs))
    # Space Complexity: O(n)
    # Datastructure(s): hash table, list/tuple
    # Algorithm(s): None
    # Pattern: Arrays & Hashing
    
    ###
    # Solve Description: Create a dictionary storing lists. The keys of the dictionary
    #   are tuples of a count array that stores the count of each letter. For each string in 
    #   strs, create a count array. Count each char in the current string and store in the
    #   count array. Turn the count array into a tuple, using it as a key in the dictionary
    #   to store the current string. After all strings have been stored in the dictionary, 
    #   return all the dictionary values in a list.
    ###
    
    # Link: https://leetcode.com/problems/group-anagrams/