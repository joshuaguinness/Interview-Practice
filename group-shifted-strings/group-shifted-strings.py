class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        groups = {}

        for string in strings:
            new_string = 'a'
            i = 1
            if len(string) == 1:
                if 'a' in groups:
                    groups['a'].append(string)
                else:
                    groups['a'] = [string]
            else:
                while i < len(string):
                    print(string, ord(string[i]), ord(string[i-1]))
                    number = ord(string[i]) - ord(string[0])
                    if number < 0: 
                        number = 123 + number
                        new_string += chr(number)
                    else:
                        new_string += chr(ord('a') + number)
                    i += 1

                if new_string in groups:
                    groups[new_string].append(string)
                else:
                    groups[new_string] = [string]
        
        print(groups.values())
        return groups.values()