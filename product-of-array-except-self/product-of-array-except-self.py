class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []
        
        p = 1
        left_array = []
        left_array.append(p)
        
        for i in range(1,len(nums)):
            left_array.append(p * nums[i-1])
            p = left_array[i]
        
        p = 1
        right_array = [1]*(len(nums))
        
        for i in range(len(nums)-2,-1,-1):
            right_array[i] = (p*nums[i+1])
            p = right_array[i]
        
        answer = []
        for i, v in enumerate(left_array):
            answer.append(v * right_array[i])
            
            
        return answer
            
        
            
        