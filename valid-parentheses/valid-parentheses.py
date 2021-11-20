class Solution:
    def isValid(self, s: str) -> bool:
        
        if (len(s) <= 1):
            return False
        
        stack = []
        
        # Using Stack With Dictionary
        
        dict = {'{': '}', '(': ')', '[': ']'}
        
        for char in s:
            if char in dict.keys():
                stack.append(char)
            elif char in dict.values():
                if (stack == []):
                    return False
                else:
                    recent = stack.pop()
                    if (dict[recent] != char):
                        return False
                
        return (stack == [])
        
        
        # Using Stack Without Dictionary
        
#         for char in s:
#             if (char == '(' or char == '{' or char == '['):
#                 stack.append(char)
#             else:
#                 if (len(stack) == 0):
#                     return False
#                 elif (char == ')'):
#                     if (stack[-1] != '('):
#                         return False
#                     stack = stack[:-1]
#                 elif (char == '}'):
#                     if (stack[-1] != '{'):
#                         return False
#                     stack = stack[:-1]
#                 elif (char == ']'):
#                     if (stack[-1] != '['):
#                         return False
#                     stack = stack[:-1]

#         return len(stack) == 0