import numpy

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        # Linear search -- easy solution, but slow O(n^2)
#         i = 1
#         while True:
#             cumm_sum = 0
#             for j, v in enumerate(nums):
#                 cumm_sum += numpy.ceil(v / i)
                
#             if cumm_sum <= threshold:
#                 return i
                
#             i += 1

        # Binary search -- much faster O(n log n)
        l = 1
        h = max(nums)
        while l < h:
            divisor = (l + h) // 2
            
            # Iterate through nums array and sum all elements / divisor
            cumm_sum = 0
            for j, v in enumerate(nums):
                cumm_sum += numpy.ceil(v / divisor)
                
            # Set new bounds
            if cumm_sum <= threshold:
                h = divisor
            else:
                l = divisor + 1
                
        return l