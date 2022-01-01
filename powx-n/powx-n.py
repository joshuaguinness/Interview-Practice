class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def Pow(x, n):
            if n == 0:
                return 1
            
            half = Pow(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        if n < 0:
            n = abs(n)
            x = 1 / x
            
        return Pow(x, n)
        
        
#         result = 1
        
#         if n > 0:
#             for i in range(n):
#                 result = result * x
#         else:
#             for i in range(abs(n)):
#                 result = result * 1/x

#         return result