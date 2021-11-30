import numpy as nmp

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        
        # If odd number
        if (len(s)) % 2 == 1:
            # Round down, then add 1 to iterate all the way up to, and including
            # the median number
            while i < len(s)//2 + 1:
                # Swap
                s[i], s[-i-1] = s[-i-1], s[i]
                i+=1
        # If even number
        else:
            while i < len(s)//2:
                s[i], s[-i-1] = s[-i-1], s[i]
                i+=1
            
        """
        Do not return anything, modify s in-place instead.
        """
        