class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # x^n = x^(n/2) * x^(n/2)
        # Therefore, only do half the work each recursive call
        def Pow(x, n):
            if n == 0:
                return 1
            half = Pow(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        # If n is negative, ensure n is positive and x is 1/x
        # This is how negative powers work
        if n < 0:
            n = abs(n)
            x = 1 / x
            
        return Pow(x, n)
        
        # Slow O(n), iterative solution
        # result = 1
        # if n > 0:
        #     for i in range(n):
        #         result = result * x
        # else:
        #     for i in range(abs(n)):
        #         result = result * 1/x
        # return result