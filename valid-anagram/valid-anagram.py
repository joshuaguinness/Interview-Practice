class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)
        
        # counter1.sort()
        # counter2.sort()
        
        return counter1 == counter2
        
        