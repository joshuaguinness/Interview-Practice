class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        output = []
        curr_line = []
        l_remaining = maxWidth
        
        # Iterate through each word
        i = 0
        while i < len(words):
            word = words[i]
            
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
                
                # Only one word on that line
                if len(curr_line) == 1:
                    # Add to output with extra spaces on end
                    output.append(curr_line[0] + " "*l_remaining)
                    # Reset variables
                    l_remaining = maxWidth
                    curr_line = []
                    continue
                
                # Calculate the spaces to add between each word
                # and add them in the loop
                num_spaces = l_remaining // (len(curr_line)-1)
                for j in range(len(curr_line)-1):
                    curr_line[j] += " "*num_spaces
                    
                # Calculate any extra spaces to add starting from the left
                num_spaces_2 = l_remaining % (len(curr_line)-1)
                for j in range(num_spaces_2):
                    curr_line[j] += " "
                    
                # Add to output the justified line
                output.append("".join(curr_line))
                
                # Reset variables
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