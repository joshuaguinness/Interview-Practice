class MedianFinder:

    def __init__(self):
        # Max heap to store the smaller half of numbers
        self.lo = []
        # Min heap to store the larger half of numbers
        self.hi = []
        
    def addNum(self, num: int) -> None:\
        # Add number to max-heap lo. Since its a max-heap,
        # we had the negative of the number
        heapq.heappush(self.lo, -num)
        
        # Performing balancing step for hi, remove largest element
        # from lo and push it to hi
        elem = heapq.heappop(self.lo)
        heapq.heappush(self.hi, -elem)
        
        # If min-heap hi has more elements than lo, fix
        # by removing smallest element from hi and pushing it
        # onto lo
        if len(self.lo) < len(self.hi):
            elem2 = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -elem2)

    def findMedian(self) -> float:
        
        # If lo > hi, median is top of lo
        # otherwise, its an average of the top of both heaps
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (-self.lo[0] + self.hi[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()