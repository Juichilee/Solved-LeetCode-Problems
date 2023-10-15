class MedianFinder:

    def __init__(self):
        # two heaps, large and small, minheap, maxheap
        # heaps should be about equal size
        self.small, self.large = [], []

    # Time Complexity: O(log(n))
    def addNum(self, num: int) -> None: 
        # heapq is python's implemented heap (min heap)
        heapq.heappush(self.small, -1 * num) # since max heap isn't implemented by python, have to multiply by -1

        # make sure every num small is <= every num in large
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]): # [0]th index is max/min value. multiply by -1 to get true max value
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size?
        if (len(self.small) > len(self.large) + 1):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if (len(self.large) > len(self.small) + 1):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    # Time Complexity: O(1)
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return (-1 * self.small[0])
        if len(self.small) < len(self.large):
            return self.large[0]
        return ((-1 * self.small[0]) + self.large[0]) / 2        
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

    # Space Complexity: O(n)
    # Datastructure(s): Heap
    # Algorithm(s): None
    # Pattern: Heap
    
    # Link: https://leetcode.com/problems/find-median-from-data-stream/