class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        missing = []
    
        if not nums:
            if lower == upper:
                missing.append(str(lower))
            else:
                missing.append(str(lower) + "->" + str(upper))
            return missing
            
        if nums[0] - lower > 1:
            missing.append(str(lower) + "->" + str(nums[0]-1))
        elif nums[0] - lower == 1:
            missing.append(str(lower))
    
        i = 0
        while i < len(nums)-1 and len(nums) > 1:
            if nums[i+1] - nums[i] > 1:
                if nums[i+1] - nums[i] > 2:
                    missing.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
                else:
                    missing.append(str(nums[i] + (nums[i+1] - nums[i] - 1)))
            i += 1
            
        if upper - nums[-1] > 0:
            if upper - nums[-1] > 1:
                missing.append(str(nums[-1]+1) + "->" + str(upper))
            else:
                missing.append(str(upper))
        
        return missing