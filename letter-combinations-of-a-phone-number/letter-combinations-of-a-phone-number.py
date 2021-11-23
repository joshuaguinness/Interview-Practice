class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        combos = []
        
        if not digits:
            return combos
        
        my_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
                  6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        helper(digits, 0, my_dict, "", combos)
        return combos
        
def helper(digits, i, mapping, string, combos):
    if (i == len(digits)):
        combos.append(string)
        return
    for char in mapping[int(digits[i])]:
        helper(digits, i+1, mapping, string+char, combos)