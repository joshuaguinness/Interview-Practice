# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        def binarySearch(row, lo, hi):
            while lo < hi:
                mid = (lo + hi) // 2
                # Its on the left side
                if binaryMatrix.get(row, mid) == 1:
                    hi = mid
                # its on the right side
                else:
                    lo = mid + 1
                
            return lo
        
        rows, cols = binaryMatrix.dimensions()
        # Initialize leftmost column with the number of columns
        leftmost = cols
        
        # Iterate through each row
        for i in range(rows):
            # Last element in row is zero means
            # that there is no 1 in the entire row,
            # move to the next row
            if binaryMatrix.get(i, cols-1) == 0:
                continue
            # There is a 1 in this row, binary search
            # to find it
            else:
                index = binarySearch(i, 0, cols-1)
                leftmost = min(leftmost, index)
        
        # No 1's
        if leftmost == cols:
            return -1
        else:
            return leftmost
        
        
# 0 0 1 1 1

# lo = 0, hi = 