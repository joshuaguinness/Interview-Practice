class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1
        
        while i < j:
                       
            char1 = s[i]
            char2 = s[j]
            
            if (char1 != char2):
                # Split remaining string into two splices
                # includes i and excludes j
                string_pos_1 = s[i:j]
                # includes j and excludes i
                string_pos_2 = s[i+1:j+1]
                # if one of these is a valid palindrome, then return True
                return string_pos_1 == string_pos_1[::-1] or string_pos_2 == string_pos_2[::-1]
            
            i += 1
            j -= 1
                
        return True