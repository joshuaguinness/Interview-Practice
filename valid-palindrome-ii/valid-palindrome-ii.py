class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # One pointer from left to right
        # Another pointer from right to left
        # compare them, if same okay
        # if not same, add one to keep tracking
        # if need to add more than 1, return false
        # if both are at same index and keep track <= 1 return true
        
        keep_track = 0
        i = 0
        j = len(s) - 1
        
        while i < j:
                       
            char1 = s[i]
            char2 = s[j]
            
            if (char1 != char2):
                string_pos_1 = s[i:j]
                string_pos_2 = s[i+1:j+1]
                print(string_pos_1, string_pos_2)
                return string_pos_1 == string_pos_1[::-1] or string_pos_2 == string_pos_2[::-1]
            
            i += 1
            j -= 1
                
        return True