class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # Binary search
        # If element is larger neighbour on the right, then limit
        # search space by cutting off that side
        # Else cut off the left side

        if len(nums) == 1:
            return 0
        
        lo = 0
        hi = len(nums)-1
        
        while lo < hi:
            mid = (hi + lo) // 2
            
            if nums[mid] > nums[mid+1]:
                hi = mid
            else:
                lo = mid + 1
        return lo


