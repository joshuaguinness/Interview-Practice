class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        # k is more than all the cuts that can be possibly made (splitting everything into length of 1)
        if k > sum(ribbons):
            return 0
        
        # k is the same length as ribbons, therefore just return minimum of ribbons
        # if len(ribbons) >= k:
        #     return min(ribbons)
        
        # Binary search on space [1 min(ribbons)] to find the maximum length
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
            
            # if sum_num_ribbons < k:
            #     high = mid-1   
            # else:
                # low = mid
                
        return low
    
    
    
#     class Solution:
#     def maxLength(self, ribbons: List[int], k: int) -> int:
#         total = sum(ribbons)
#         if k > total:
#             return 0
        
#         lo, hi = 1, min(total // k, max(ribbons))
        
#         while lo < hi:
#             mid = (lo + hi + 1) // 2
#             if sum(x // mid for x in ribbons) >= k:
#                 lo = mid
#             else:
#                 hi = mid - 1
        
    
    