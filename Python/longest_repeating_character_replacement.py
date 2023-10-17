class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize count dict, left pointer, res, and max_freq
        count = {} # letter: count
        l = 0
        res = 0
        max_freq = 0

        # one-pass right pointer
        for r in range(0, len(s)):
            # add 1 to letter count in count dict
            count[s[r]] = 1 + count.get(s[r], 0)
            # Check if current letter's freq is greater than max_freq and update O(1) time
            max_freq = max(max_freq, count[s[r]])
            # As long as length - maxf <= k, do not have to update hash table, thus reducing O(26 * n) to O(n)
            while ((r - l + 1) - max_freq > k):
                # remove letter at l from count_dict and increment l by 1
                count[s[l]] -= 1
                l += 1
            
            # current length should fit within parameters. update res with longer length
            res = max(r - l + 1, res)
        
        return res
                
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): hash table
    # Algorithm(s): none
    # Pattern: Sliding Window

    ###
    # Solve Description: Initialize a count hash table mapping a letter to its count in the string and a max_frequency. 
    #   Using the Sliding Window method, keep incrementing the right pointer and update the letter count in the hash 
    #   table for the current letter and the max letter frequency. Then, run a while loop maintaining the condition that 
    #   as long as (window_size - max_freq > k), increment the left pointer and update the count hash table. Update the 
    #   var storing results if the current window_size is greater
    ###
    # Link: 