class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        length = len(nums)
        if length == 0:
            return [-1, -1]
        
        l = 0
        r = length - 1
        mid = 0
        
        # Binary search
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        # mid position = target
        if nums[mid] == target:
            l = mid
            r = mid
        # l position = target
        elif nums[l] == target:
            r = l
        # if mid or l are not target, then doesn't exist in the array
        else:
            return [-1, -1]
        
        # Start left and right at the target and iterate in each direction
        # until the value is no longer the target value, that will give
        # the left and right bounds of the target value
        while l-1 >= 0 and nums[l-1] == target:
            l -= 1
        while r+1 < length and nums[r+1] == target:
            r += 1
        return [l, r]
    
    # Optimal solution is to do two binary searches
    # one for low, the other for high, then just return
    # [low, high]. See solution for more details.