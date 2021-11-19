class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        # Save having to run through entire loop if same number
        if (x == y):
            return 0
        
        num_diff = 0
        
        # Get possible length of the two binary representations to format
        # the string with least number of possible digits
        length = max(len(bin(x)), len(bin(y)))
        x_string = format(x, "0"+str(length)+"b")
        y_string = format(y, "0"+str(length)+"b")
        
        
        # Iterate through the string and compare characters
        for i, c in enumerate(x_string):
            if (c != y_string[i]):
                num_diff += 1
        
        return num_diff
        