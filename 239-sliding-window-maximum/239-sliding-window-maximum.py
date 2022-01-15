class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        if n * k == 0:
            return []        
        if k == 1:
            return nums
    
        # Simple queue solution O(n^2) -- i think
        # queue = deque([])
        # max_list = []
        # for i in range(k):
        #     queue.append(nums[i])
        # max_list.append(max(queue))
        # for i in range(k, len(nums)):
        #     queue.popleft()
        #     queue.append(nums[i])
        #     max_list.append(max(queue))
        # return max_list
        
        
        # Monotonically Increasing Queue Solution
        queue = deque([])
        res = []
        
        for i in range(len(nums)):
            
            # If left element in queue is out of bounds, pop it to maintain size
            if i-k >= 0 and nums[i-k] == queue[0]:
                queue.popleft()
                
            # Ensures array is decreasing, pops elements that are smaller
            while queue and queue[-1] < nums[i]:
                queue.pop()
                
            # add the element
            queue.append(nums[i])
            
            # Append to result list when have full window
            if i >= k-1:
                res.append(queue[0])
                
        return res

    
        # DP - right array then left array approach
        # See solution tab for more details
#         left = [0] * n
#         left[0] = nums[0]
#         right = [0] * n
#         right[n-1] = nums[n-1]
        
#         # From left to right
#         for i in range(1, n):
#             if i % k == 0:
#                 # New block starts
#                 left[i] = nums[i]
#             else:
#                 # Compare to previous to get max
#                 left[i] = max(left[i-1], nums[i])
            
#         # From right to left
#         for i in range(n-2, -1, -1):
#             if i % k == k-1:
#                 # Block starts
#                 right[i] = nums[i]
#             else:
#                 right[i] = max(right[i+1], nums[i])
        
#         res = []
#         # Compare beginning and ends of each window
#         for i in range(0, n-k+1):
#             res.append(max(left[i+k-1], right[i]))
#         return res