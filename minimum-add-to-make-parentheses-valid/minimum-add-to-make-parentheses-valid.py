class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        count = 0
        
        for i,v in enumerate(s):
            if v == '(':
                stack.append('(')
            if v == ')':
                if stack == []:
                    count += 1
                    continue
                else:
                    stack.pop()
        
        return count + len(stack)
        
        # (())(()()
        