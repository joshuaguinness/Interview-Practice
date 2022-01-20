class Solution:
    def calculate(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        s = s.replace(" ", "")
        
        current_op = "+"
        current_number = 0

        stack = []
        total = 0
        
        i = 0
        while i < len(s):
            
            if s[i].isdigit():
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j += 1

                current_number = int(s[i:j])
                # stack.append()
                if j == len(s):
                    i = j -1
                else:
                    i = j   
            
            if not s[i].isdigit() or i == len(s)-1:
                if current_op == "+":
                    stack.append(current_number)
                    
                elif current_op == "-":
                    stack.append(-current_number)

                elif current_op == "*":
                    prev_number = stack.pop()
                    res = prev_number * current_number
                    stack.append(res)

                elif current_op == "/":
                    prev_number = stack.pop()
                    # res = prev_number // current_number
                    res = int(float(prev_number)/current_number)
                    # print("result", res)
                    stack.append(res)
                    # if prev_number < 0 or current_number < 0:
                    #     stack.append(res + 1)
                    # else:
                    #     stack.append(res)
                
                
                current_number = 0
                current_op = s[i]
                i += 1  
            

        print(stack)
        if len(stack) > 0:
            total += sum(stack)
        
        return total
                
            
                
        
        