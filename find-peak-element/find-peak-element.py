class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # Binary search
        # If element is larger than both of neighbours return the index aka peak
        # Cut off the side that is smaller

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
            
            # if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            #     return mid
            # elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
            #     lo = mid
            # elif nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]:
            #     hi = mid
            # else:
            #     hi = mid
        
        # lo = 1, hi = 3
        # mid = 2
        
        
# lo = 0, hi = 6, mid = 3
# lo = 3, hi = 6, mid = 4
# lo = 4, hi = 6, mid = 5

# lo = 0, hi = 1, mid = 0

