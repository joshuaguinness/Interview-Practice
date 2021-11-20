class Solution:
    def isValid(self, s: str) -> bool:
        
        if (len(s) <= 1):
            return False
        
        stack = []
        
        for char in s:
            if (char == '(' or char == '{' or char == '['):
                stack.append(char)
            if (char == ')' or char == '}' or char == ']'):
                if (len(stack) == 0):
                    return False
            if (char == ')'):
                if (stack[-1] != '('):
                    return False
                stack = stack[:-1]
            if (char == '}'):
                if (stack[-1] != '{'):
                    return False
                stack = stack[:-1]
            if (char == ']'):
                if (stack[-1] != '['):
                    return False
                stack = stack[:-1]
        
        return len(stack) == 0