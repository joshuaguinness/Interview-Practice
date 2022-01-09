class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        arr = [0]*length
        
        for i, v in enumerate(updates):
            start, end, val = v
            
            arr[start] += val
            if end < length - 1:
                arr[end + 1] -= val
                
        i = 1
        while i < length:
            arr[i] = arr[i] + arr[i-1]
            i += 1
            
        return arr
            