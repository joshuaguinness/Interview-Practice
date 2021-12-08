class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Dictionary of string to values
        # Iterate backwards through string
        # add the two numbers
        
        # my_dict = {"0": 0, ""}
        
        i, j = len(num1)-1, len(num2)-1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry > 0:
            num1_val = 0 if i < 0 else int(num1[i]) # python ternary operator
            num2_val = 0 if j < 0 else int(num2[j])
            unit_res = num1_val + num2_val + carry
            carry, unit_res = divmod(unit_res, 10)
            res.append(unit_res)
            i -= 1
            j -= 1
        
        res_str = ""
        for val in res[::-1]:
            res_str += str(val)
        return res_str
        