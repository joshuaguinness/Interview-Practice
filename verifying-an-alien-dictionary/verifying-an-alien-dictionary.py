class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        my_dict = {}
        
        def compare(word1, word2):
            in_order = True
            for i, char in enumerate(word1):
                if i >= len(word2):
                    return False
                elif my_dict[char] < my_dict[word2[i]]:
                    break
                elif my_dict[char] == my_dict[word2[i]]:
                    continue
                else:
                    return False
            return True
        
        # Add the alphabet order to a dictionary
        i = 1
        for char in order:
            my_dict[char] = i
            i += 1
        
        j = 0
        while j < len(words) - 1:
            # Compare jth word and jth+1 word
            if not compare(words[j], words[j+1]):
                return False
            j += 1
            
        return True
            