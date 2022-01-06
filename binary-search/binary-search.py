class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        
        # if len(nums) == 1:
        #     if nums[0] == target:
        #         return 0
        #     else:
        #         return -1
        
        while l < r:
            mid = (l + r) // 2
            
            print(mid)
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        if nums[l] == target:
            return l
        else:
            return -1