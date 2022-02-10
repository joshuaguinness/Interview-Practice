class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
                
        # Get the minimum length of all the strings
        min_len = 200
        for i, v in enumerate(strs):
            min_len = min(min_len, len(v))
        
        i = 0
        prefix = ""
        
        # Max length of prefix would be the minimum
        # length of string in the array
        while i < min_len:
            
            # The first character at the index, this is
            # the one we want to check with all other characters
            # at that index in the strings in the array
            char = strs[0][i]
            
            for j, v in enumerate(strs):
                # Character at index doesn't match the comparison character
                if v[i] != char:
                    return prefix
            
            i += 1    
            
            # Add the character to the prefix
            prefix = prefix + char
            
        return prefix