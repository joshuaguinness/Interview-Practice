class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # Iterate through both word and abbr at the same time
        # When get to a number, skip a number of iterations
        # If at any points the two characters don't match, return false
        
        i = 0 # Iterator for word
        j = 0 # Iterator for abbr
        
        while i < len(word) and j < len(abbr):
            
            print(i, j)
            print(word[i], abbr[j])
            
            if abbr[j].isdigit():
                
                # Leading zeros and empty substring
                if int(abbr[j]) == 0:
                    return False
                
                if j < len(abbr)-1:
                    if abbr[j+1].isdigit():
                        jump = int(abbr[j:j+2])
                        if (jump > len(word) - i):
                            return False
                        i += jump
                        j += 2
                    else:
                        i += int(abbr[j])
                        j += 1
                else:
                    i += int(abbr[j])
                    j += 1
                    
            if (i >= len(word)):
                if (i - len(word) == j - len(abbr)):
                    return True
                else:
                    return False
                
            if (j >= len(abbr) and i < len(word)):
                return False
                
                
            if word[i] != abbr[j]:
                return False
        
            i += 1
            j += 1

        if (len(abbr)) > j:
            return False
        
        if (len(word)) > i:
            return False
            
        return True
        