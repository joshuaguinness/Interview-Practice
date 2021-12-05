class SparseVector:
    # Approach 1: Array of vectors, brute force but faster approach
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for i, v in enumerate(self.nums):
            product += v*vec.nums[i]
        return product
    
    # Appraoch 2: Storing <index, value> pairs, slower approach
#     def __init__(self, nums: List[int]):
#       # Add only values that aren't 0 storing their index as well    
#         self.indexvalue = []
#         for i, v in enumerate(nums):
#             if v != 0:
#                 self.indexvalue.append([i, v])
                
#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         product = 0
#         i = 0
#         j = 0
#         while i < len(self.indexvalue) and j < len(vec.indexvalue):

#             # They have the same index
#             if (self.indexvalue[i][0] == vec.indexvalue[j][0]):
#                 product += self.indexvalue[i][1] * vec.indexvalue[j][1]
#                 i += 1
#                 j += 1
#           # Index of i < index of j, increase i
#             elif (self.indexvalue[i][0] < vec.indexvalue[j][0]):
#                 i += 1
#             else:
#                 j += 1
            
#         return product
            

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)