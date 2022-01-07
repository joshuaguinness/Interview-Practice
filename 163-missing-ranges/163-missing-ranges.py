class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        missing = []
    
        # nums doesn't exist
        # Append to missing array depending on whether 
        # upper and lower equal each other
        if not nums:
            if lower == upper: missing.append(str(lower))
            else: missing.append(str(lower) + "->" + str(upper))
            return missing
            
        # Adding possible missing ranges before first element
        if nums[0] - lower > 1: missing.append(str(lower) + "->" + str(nums[0]-1))
        elif nums[0] - lower == 1: missing.append(str(lower))
    
        i = 0
        # Iterate through and add any possible missing ranges between elements
        while i < len(nums)-1 and len(nums) > 1:
            if nums[i+1] - nums[i] > 2:
                missing.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
            elif nums[i+1] - nums[i] == 2:
                missing.append(str(nums[i] + (nums[i+1] - nums[i] - 1)))
            i += 1
            
        # Adding possible missing ranges after last element
        if upper - nums[-1] > 1: missing.append(str(nums[-1]+1) + "->" + str(upper))
        elif upper - nums[-1] == 1: missing.append(str(upper))
        
        return missing