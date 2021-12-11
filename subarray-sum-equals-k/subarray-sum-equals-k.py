class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Using HashMap
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