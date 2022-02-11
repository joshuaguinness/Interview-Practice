class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        # Traditional
        # ans = []
        # for i, v in enumerate(nums):
        #     ans.append(nums[nums[i]])
        # return ans
        
        # List comprehension
        return [nums[x] for x in nums]