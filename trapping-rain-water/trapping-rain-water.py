class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Brute Force Solution
#         ans = 0
#         for i, v in enumerate(height):
#             left_max = 0
#             right_max = 0
#             for j in range(0, i):
#                 left_max = max(left_max, height[j])
#             for j in range(i+1, len(height)):
#                 right_max = max(right_max, height[j])          
#             water_above = min(left_max, right_max) - height[i]
#             if water_above > 0:
#                 ans += water_above 
#         return ans

        # Using a stack approach and one pass solution
        ans = 0
        current = 0
        stack = []
        while (current < len(height)):
            while stack != [] and height[current] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if (stack == []):
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(current)
            current += 1
            
        return ans
            
            
        