class Solution:
    def calculate(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        # Remove all extra spaces
        s = s.replace(" ", "")
        
        current_op = "+"
        current_number = 0

        stack = []

        i = 0
        while i < len(s):
            
            # Current character is a digit
            if s[i].isdigit():
                
                # Number may be made up of multiple digits, get
                # all of them
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j += 1

                # This is now the current number
                current_number = int(s[i:j])
                
                # Depending on the j value here, if its the
                # last index, we want the next if statement to execute
                # so reducing it by one will not cause an error
                if j == len(s):
                    i = j - 1
                else:
                    i = j   
            
            # Current character is an operation, or
            # its the end of the input string
            if not s[i].isdigit() or i == len(s)-1:
                if current_op == "+":
                    stack.append(current_number)
                    
                elif current_op == "-":
                    # Add negative value
                    stack.append(-current_number)

                elif current_op == "*":
                    prev_number = stack.pop()
                    res = prev_number * current_number
                    stack.append(res)

                elif current_op == "/":
                    prev_number = stack.pop()
                    # Due to weird python division behaviour with negative numbers
                    res = int(float(prev_number)/current_number)
                    stack.append(res)
                
                current_number = 0
                current_op = s[i]
                i += 1  
        
        # Sum up all the remaining values in the stack
        total = 0
        if len(stack) > 0:
            total += sum(stack)
        
        return total
                
            
                
        
        