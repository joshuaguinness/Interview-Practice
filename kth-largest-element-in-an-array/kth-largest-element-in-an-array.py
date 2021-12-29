class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Using Sorting
        # nums.sort(reverse=True)
        # return nums[k-1]
    
        # Using Heap
        return heapq.nlargest(k, nums)[-1]