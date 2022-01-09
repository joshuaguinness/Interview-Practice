class Solution:
    def maximumSwap(self, num: int) -> int:
        
        # Iterate through the string until find
        # first number that is larger than the prev
        # aka iterate until no longer decreasing
        # Then find the max of remaining numbers
        # Then insert that max number as high as possible in
        # the first part of the number
        
        # Convert num to a list of string digits
        nums = list(map(str, str(num)))
        local_max = -1
        max_index = -1
        it_start = -1
        
        # Iterate through the nums array
        for i, v in enumerate(nums):
            
            # Numbers are no longer decreasing
            if i < len(nums)-1 and v < nums[i+1]:
                
                # Index to start iterating at
                # when searching for value to swap
                it_start = i
                
                # Find the max of the rest of the array
                # iterate backwards so it finds the last max
                for j in range(len(nums)-1, i, -1):
                    if (int(nums[j]) > int(local_max)):
                        local_max = nums[j]
                        max_index = j
                break
        
        # num is already the max, no swaps can
        # make it higher
        if local_max == -1:
            return num
        
        # Iterate from the index where the digits
        # Stoped decreasing to the beginning to find
        # the element that the max should be swapped with
        i = it_start
        while i > 0 and local_max > nums[i-1]:
            i -= 1
        
        # Swap the numbers
        nums[i], nums[max_index] = nums[max_index], nums[i]
        
        # Return
        return int("".join(nums))