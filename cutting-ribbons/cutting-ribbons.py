class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        # k is more than all the cuts that can be possibly made (splitting everything into length of 1)
        if k > sum(ribbons):
            return 0
        
        # Binary search on space [1 max(ribbons)] to find the maximum length
        low = 1
        high = max(ribbons)
        
        while low < high:
            mid = (low + high + 1) // 2
            
            sum_num_ribbons = 0
            for ribbon in ribbons:
                sum_num_ribbons += ribbon // mid
                
            if sum_num_ribbons >= k:
                low = mid
            else:
                high = mid - 1
                
        return low