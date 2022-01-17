class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        my_dict = {}
        split_s = s.split(' ')
        
        if len(pattern) != len(split_s):
            return False
        
        for i, v in enumerate(pattern):
            
            string_val = split_s[i]
            
            if v in my_dict:
                if my_dict[v] != string_val:
                    return False
            else:
                if string_val not in my_dict.values():
                    my_dict[v] = string_val
                else:
                    return False
                
        return True