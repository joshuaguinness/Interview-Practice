class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        # Prefix sum solution. See solution tab
        # for more details.
        p = [0]
        for digit in s:
            p.append(p[-1] + int(digit))
        
        # Array of number of flips required for 
        # x number of zeros
        poss = []
        
        length = len(s)
        for i in range(length+1):
            poss.append(p[i] + (length - i) - (p[-1] - p[i]))
            
        return min(poss)