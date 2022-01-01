class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        my_dict = {}
        
        # Compare word1 and word2 to see if correct order
        def compare(word1, word2):
            
            # Enumerate through the first word
            for i, char in enumerate(word1):
                # If word2 is shorter than word1
                # We know it is out of order and word2
                # should go before word1
                if i >= len(word2):
                    return False
                # Two characters are in correct order
                # Therefore words are in correct order
                elif my_dict[char] < my_dict[word2[i]]:
                    break
                # Two characters are the same
                elif my_dict[char] == my_dict[word2[i]]:
                    continue
                # Characters are out of order, therefore words are too
                else:
                    return False
            return True
        
        # Add the alphabet order to a dictionary
        # <key, value> = <letter, order>
        i = 1
        for char in order:
            my_dict[char] = i
            i += 1
        
        # Loop through the list and compare adjacent words
        # By verifying adjacent words are in correct order, we verify
        # that the entire order is correct
        j = 0
        while j < len(words) - 1:
            # Compare jth word and jth+1 word
            if not compare(words[j], words[j+1]):
                return False
            j += 1
            
        return True