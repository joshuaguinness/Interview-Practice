class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Using HashMap, O(n)
        my_map = {0: 1}
        cumm_sum = 0
        count = 0
        for i, v in enumerate(nums):
            cumm_sum += nums[i]
            if (cumm_sum - k in my_map.keys()):
                count += my_map[cumm_sum - k]
            if cumm_sum in my_map.keys():
                my_map[cumm_sum] += 1
            else:
                my_map[cumm_sum] = 1
        return count

        # Using Cummulative Sum, O(n^2)
#         count = 0
#         cumm_sum = [0]
#         for i in range(1,len(nums)+1):
#             cumm_sum.append(cumm_sum[i-1] + nums[i-1])
#         for i in range(0, len(nums)+1):
#             for j in range(i+1,len(nums)+1):
#                 if (cumm_sum[j] - cumm_sum[i] == k):
#                     count += 1   
#         return count