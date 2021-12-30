class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # Create two arrays: one for digits and one for letters
        letter_array = []
        digit_array = []
        
        for log in logs:
            
            # Split the log at spaces
            split_log = log.split(' ')
            
            # If reach a digit log, just append to the array
            if split_log[1].isdigit():
                digit_array.append(log)
            # If reach a letter log, just append to array
            else:
                letter_array.append(log)
                
        # Sort the letter logs in alphabetical order by their contents
        letter_array.sort(key=lambda x: (' '.join(x.split(' ')[1:]), x.split(' ')[0]))
        
        # For identical letter conents, sort by identifier
        # i = 0
        # while i < len(letter_array)-1:
        #     while (letter_array[i].split(' ')[1:] == letter_array[i+1].split(' ')[1:]):
                
                
        
        # Combine the two arrays and return
        return letter_array + digit_array
        