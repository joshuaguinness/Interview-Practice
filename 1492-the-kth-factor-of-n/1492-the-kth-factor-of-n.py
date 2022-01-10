class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        # O(n) solution, simple and works but can be done better
        # factors = []
        # for i in range(1, n+1):
        #     if n % i == 0:
        #         factors.append(i)
        # if k > len(factors):
        #     return -1
        # else:
        #     return factors[k-1]
        
        # Heap Solution
        heap = []
        # Iterate up to the square root (covers all values)
        for i in range(1, int(n**0.5) + 1):
            
            # Divisible with no remainder add
            if n % i == 0:
                heapq.heappush(heap, i)
                # Ensure don't add same value twice
                if i != n // i:
                    heapq.heappush(heap, n//i)
         
        if k > len(heap):
            return -1
        else:
            return heapq.nsmallest(k, heap)[-1]