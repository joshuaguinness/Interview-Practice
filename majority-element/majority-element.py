class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Using Boyer-Moore Majority Vote Algorithm
        
        count = 1
        major = nums[0]

        for i in range(1,len(nums)):
            if (nums[i] != major):
                count -= 1
                if (count == 0):
                    major = nums[i]
                    count += 1
            else:
                count += 1
                
        return major
        
        # Quick and Dirty Way

        # c = Counter(nums)
        # return (c.most_common(1)[0][0])