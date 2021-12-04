class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        to_remove = set()
        new_string = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')': 
                if stack != []:
                    stack.pop()
                else:
                    to_remove.add(i)
                    
        to_remove = to_remove.union(set(stack))
            
        # Remove all extra '(' from the string
        for i, char in enumerate(s):
            if i not in to_remove:
                new_string.append(char)
                
        return "".join(new_string)
            
        
            
            
            
