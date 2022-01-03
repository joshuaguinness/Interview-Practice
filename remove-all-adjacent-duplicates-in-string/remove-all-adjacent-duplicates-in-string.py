class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i, v in enumerate(s):
                
            if stack and v == stack[-1]:
                stack.pop()
                continue
                
            stack.append(v)
            
        return "".join(stack)