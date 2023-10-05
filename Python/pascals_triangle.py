class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        curRows = 1
        while curRows < numRows:
            i = 0
            j = 1 
            newRow = []

            while (j < len(res[-1])):
                newVal = res[-1][i] + res[-1][j]
                newRow.append(newVal)
                i += 1
                j += 1

            newRow.insert(0, 1)
            newRow.append(1)
            res.append(newRow)

            curRows += 1
        
        return res
            
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Datastructure(s): Array
    # Algorithm(s): none
    # Pattern: Array
    
    # Link: https://leetcode.com/problems/pascals-triangle/