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
        # Combine the two arrays and return
        return letter_array + digit_array