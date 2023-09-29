class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedList = sorted(intervals) # make sure intervals are sorted first
        res = []
        i = 0
        while(i < len(sortedList)):
            curStart, curEnd = sortedList[i]
            j = i + 1
            while(j < len(sortedList)): 
                nextStart, nextEnd = sortedList[j]
                if(nextStart <= curEnd):
                    # get the bigger end
                    curEnd = max(curEnd, nextEnd)
                    # get the next interval to compare
                    j += 1
                else:
                    break
                
            # new interval detected, add previous curStart and curEnd to results
            res.append([curStart, curEnd])
            i = j

        return res

    # Time Complexity: O(nlog(n)) # from python sorting
    # Space Complexity: O(n)
    # Datastructure(s): Arrays
    # Algorithm(s): None
    # Pattern: Arrays, Two Pointer

    ###
    # Solve Description: Use 2 pointers i and j pointing to 2 intervals for comparison. 
    #   i only updates when there is a new interval detected. j = i + 1 and updates when 
    #   merging new intervals together. If an mergable interval is detected while updating j 
    #   (i.e., nextStart <= curEnd), update curEnd to max(curEnd, nextEnd).
    ###
    
    # Link: https://leetcode.com/problems/merge-intervals/