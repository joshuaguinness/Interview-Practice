class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        length = len(nums)
        if length == 0:
            return [-1, -1]
        
        l = 0
        r = length - 1
        mid = 0
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        if nums[mid] == target:
            l = mid
            r = mid
        elif nums[l] == target:
            r = l
        else:
            return [-1, -1]
        
        while l-1 >= 0 and nums[l-1] == target:
            l -= 1
        while r+1 < length and nums[r+1] == target:
            r += 1
        return [l, r]