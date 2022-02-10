class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        # Intuition from solution
        # Two coordinates are on same diagonal if and only if 
        # r1 - c1 == r2 - c2
        
        # Keep track of which squares/values have been seen before
        seen_before = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                # New diagonal group, add it to dictionary
                # as a key with its value being the value
                if r-c not in seen_before:
                    seen_before[r-c] = val
                    
                # Diagonal group seen before, check if
                # value in dictionary matches current value
                elif seen_before[r-c] != val:
                    return False
        return True
        
        
        