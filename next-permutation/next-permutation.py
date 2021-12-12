class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums)-2
        while i >= 0:
            if nums[i+1] > nums[i]:
                break
            i-=1
            
        print(i)
        if (i >= 0):
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]

        start = i+1
        end = len(nums)-1

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        return