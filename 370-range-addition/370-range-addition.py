class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        # Prefix sum
        # See solution tab for in depth description
        
        arr = [0]*length
        
        # Iterate through the array
        for i, v in enumerate(updates):
            start, end, val = v
            
            # Update start index with val
            arr[start] += val
            
            # Update end + 1 index with -val
            if end < length - 1:
                arr[end + 1] -= val
                
        i = 1
        # Iterate through arr
        while i < length:
            
            # Update each index with its current
            # value plus the sum of the previous value
            arr[i] = arr[i] + arr[i-1]
            i += 1
            
        return arr
