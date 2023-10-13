class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap) # min heap
        
        count = 0 
        numSize = len(nums) 

        # pop all of the smallest nums from heap until heap is size k
        while count < (numSize - k):
            heapq.heappop(heap)
            count += 1

        # return the top elem of heap, which should be kth largest
        return heap[0]

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Datastructure(s): Min Heap
    # Algorithm(s): None
    # Pattern: Heap
        
    # Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
        