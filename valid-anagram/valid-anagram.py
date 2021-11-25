class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Easy method using counter        
        # return Counter(s) == Counter(t)
    
        # Using default dictionary
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i, v in enumerate(s):
            dict1[v] += 1
        for i, v in enumerate(t):
            dict2[v] += 1
            
        return sorted(dict1.items()) == sorted(dict2.items())