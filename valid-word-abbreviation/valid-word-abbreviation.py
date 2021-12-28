class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # Iterate through both word and abbr at the same time
        # When get to a number, skip a number of iterations
        # If at any points the two characters don't match, return false
        
        i = 0 # Iterator for word
        j = 0 # Iterator for abbr
        n = len(word)
        m = len(abbr)
        
        while i < n and j < m:
            
            # Leading zeros and empty substring
            if abbr[j] == "0":
                return False
            
            # Match properly
            elif word[i] == abbr[j]:
                i += 1
                j += 1
                
            # Digits encounterd
            elif abbr[j].isdigit():
                k = j
                # Iterate until no longer any digits
                while k < m and abbr[k].isdigit():
                        k += 1
                    
                # Add number to i, add number of digits to j
                i += int(abbr[j:k])
                j = k
            
            else:
                return False
            
        return i == n and j == m
