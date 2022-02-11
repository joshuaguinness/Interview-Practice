class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        n = len(nums)
        
        # Iterate through array
        while i < n:
            # Matching value
            if nums[i] == val:
                # Bring in value from end, don't increment i (need to check new value)
                # decrease length of array being checked
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
                
        return n