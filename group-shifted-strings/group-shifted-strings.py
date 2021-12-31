class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # Main Idea:
        # Shift each string so that its first value is 'a'
        # If that reference_string exists in the dictionary
        # then append to it, if not, create the entry
        
        # Dictionary of groups of strings
        groups = {}

        # Iterate through each string
        for string in strings:
            
            # Initialize the reference string creation
            reference_string = 'a'
            
            # Length of string is 1
            if len(string) == 1:
                if 'a' in groups:
                    groups['a'].append(string)
                else:
                    groups['a'] = [string]
            
            else:
                i = 1
                # Iterate through each char in the string
                # starting with the second one
                while i < len(string):
                    
                    # Difference between current char and base char
                    diff = ord(string[i]) - ord(string[0])
                    
                    # current comes before base character
                    if diff < 0:
                        
                        # Start backwards from the alphabet, 
                        # z is 122
                        diff = 123 + diff
                        reference_string += chr(diff)
                        
                    else:
                        
                        # Add the diff + ord(a) to the reference_string
                        reference_string += chr(ord('a') + diff)
                    i += 1

                # Check if exists in dictionary. If true append,
                # if not, create a new entry
                if reference_string in groups:
                    groups[reference_string].append(string)
                else:
                    groups[reference_string] = [string]
        
        return groups.values()