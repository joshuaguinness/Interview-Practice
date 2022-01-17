class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        my_dict = {}
        split_s = s.split(' ')
        
        if len(pattern) != len(split_s):
            return False
        
        for i, v in enumerate(pattern):
            
            if v in my_dict:
                if my_dict[v] != split_s[i]:
                    return False
            else:
                if split_s[i] not in my_dict.values():
                    my_dict[v] = split_s[i]
                else:
                    return False
                
        return True