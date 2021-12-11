class Solution:

    def __init__(self, w: List[int]):
        self.sum = []
        cummulative_sum = 0
        for i,v in enumerate(w):
            cummulative_sum += v
            self.sum.append(cummulative_sum)

    def pickIndex(self) -> int:
        if (len(self.sum) == 1):
            return 0
        
        random_number = random.randint(1,self.sum[-1])

        left = 0
        right = len(self.sum)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if random_number > self.sum[mid]:
                left = mid + 1
            else:
                right = mid

        return left