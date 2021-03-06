class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # Iterate through both strings backwards
        # Add each individual number together and add it to a list
        # Don't forget to include the carry
        # Convert list to string and return
        
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry > 0:
            num1_val = 0 if i < 0 else int(num1[i]) # python ternary operator
            num2_val = 0 if j < 0 else int(num2[j])
            unit_res = num1_val + num2_val + carry
            # Nifty carry logic
            carry, unit_res = divmod(unit_res, 10)
            res.append(unit_res)
            i -= 1
            j -= 1
        
        res_str = ""
        # Don't forget to reverse since we went through backwards
        for val in res[::-1]:
            res_str += str(val)
        return res_str
        