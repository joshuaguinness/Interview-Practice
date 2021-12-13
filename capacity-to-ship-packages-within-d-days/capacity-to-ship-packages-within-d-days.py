class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        
        while low < high:
            
            mid = (low + high) // 2
            total = 0
            num_days = 1
            
            for w in weights:
                if total + w > mid:
                    num_days += 1
                    total = w
                else:
                    total += w
                    
            if num_days > days:
                low = mid + 1
            else:
                high = mid
                
        return low