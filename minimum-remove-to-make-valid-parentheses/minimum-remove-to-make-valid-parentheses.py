class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        to_remove = set()
        new_string = []
        
        # First pass, add all '(' to set, pop when get ')'
        # If get ')' with empty set, add index to set to remove
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')': 
                if stack != []:
                    stack.pop()
                else:
                    to_remove.add(i)
                    
        # Union of stack and set
        # Add all extra '(' in the stack to the set
        to_remove = to_remove.union(set(stack))
            
        # Second pass
        # Remove all extra '(' from the string
        for i, char in enumerate(s):
            if i not in to_remove:
                new_string.append(char)
                
        # Create a new string
        return "".join(new_string)
            
