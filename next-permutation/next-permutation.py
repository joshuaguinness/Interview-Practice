class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Iterate from the back and find first element that is smaller than the previous
        i = len(nums)-2
        while i >= 0:
            if nums[i+1] > nums[i]:
                break
            i-=1
            
        # Assuming i is not -1, iterate from the back and find the first element
        # that is larger than nums[i], this will be the value that the two
        # will be swapped to get the next largers
        if (i >= 0):
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the remaining i+1 elements in the array so that it really is
        # the next largest permutation
        # If the array is in descending order, this will also reverse it to be
        # in ascending order
        start = i+1
        end = len(nums)-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        return