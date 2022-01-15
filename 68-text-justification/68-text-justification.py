class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        output = []
        curr_line = []
        l_remaining = maxWidth
        
        # Iterate through each word
        i = 0
        while i < len(words):
            word = words[i]
            print(l_remaining, curr_line)
            
            # There is room on the line for the word
            if len(word) <= l_remaining:
                # Add to the current line
                curr_line.append(word)
                # Adjust length remaining (+1 for the space between words)
                l_remaining -= len(word) + 1
                i += 1
            
            # There is no space left on the line for the word, pack with spaces
            else:
                
                # Add back spaces taken off for calculation purposes
                l_remaining += len(curr_line)
                if len(curr_line) == 1:
                    output.append(curr_line[0] + " "*l_remaining)
                    l_remaining = maxWidth
                    curr_line = []
                    continue
                
                # Spaces to add between each word
                num_spaces = l_remaining // (len(curr_line)-1)
                
                for j in range(len(curr_line)-1):
                    curr_line[j] += " "*num_spaces
                    
                # Extra spaces to add starting from the left
                num_spaces_2 = l_remaining % (len(curr_line)-1)
                
                for j in range(num_spaces_2):
                    curr_line[j] += " "
                    
                output.append("".join(curr_line))
                
                l_remaining = maxWidth
                curr_line = []
                
        # Last line of text -- words should be left justified with
        # no extra space inserted between them. 
        # Add to curr_line the number of remaining spaces to add
        if l_remaining >= 0:
            output.append(" ".join(curr_line) + " "*(l_remaining+1))
        else:
            output.append(" ".join(curr_line))

        return output