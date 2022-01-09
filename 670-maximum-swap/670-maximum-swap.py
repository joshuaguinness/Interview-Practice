class Solution:
    def maximumSwap(self, num: int) -> int:
        
        # Iterate through the string until find
        # first number that is larger than the prev
        # aka iterate until no longer decreasing
        # Then find the max of remaining numbers
        # Then insert that max as high as possible in
        # the decreasing numbers first part
        
        nums = list(map(str, str(num)))
        local_max = -1
        max_index = -1
        it_start = -1
        for i, v in enumerate(nums):
            if i < len(nums)-1 and v < nums[i+1]:
                it_start = i
                # Find the max of the rest of the array
                # iterate backwards so it finds the last max
                for j in range(len(nums)-1, i, -1):
                    if int(nums[j]) > int(local_max):
                        local_max = nums[j]
                        max_index = j
                # local_max = max(nums[i+1:])
                # max_index = nums[i+1:].index(local_max) + (i + 1)
                break
        
        print(max_index, local_max)
        print(it_start)
        
        # num is already the max, no swaps can
        # make it higher
        if local_max == -1:
            return num
        
        # i = max_index
        i = it_start
        while i > 0 and local_max > nums[i-1]:
            i -= 1
        # Iterate from other side
        
        # while i < len(nums)-1 and local_max > nums[i]
        
        print(i)
        # if i != 0:
        #     i += 1
        nums[i], nums[max_index] = nums[max_index], nums[i]
        
        return int("".join(nums))
            
  # 32176
  # 73216