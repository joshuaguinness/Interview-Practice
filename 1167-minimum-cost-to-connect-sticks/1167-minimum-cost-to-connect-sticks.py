class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        cost = 0
        
        # Convert sticks into a heap
        heapq.heapify(sticks)
        
        # Until the heap has one element
        while len(sticks) > 1:
            
            # Pop the two smallest
            small_1 = heapq.heappop(sticks)
            small_2 = heapq.heappop(sticks)
            
            # Create a new stick
            new_stick = small_1 + small_2
            
            # Add cost of new stick to cost
            cost += new_stick
            
            # Add new stick back to heap
            heapq.heappush(sticks, new_stick)
            
        return cost
            