import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict = {}
        
        for number in nums:
            if number in my_dict:
                my_dict[number] += 1
            else:
                my_dict[number] = 1
             

        most_common = collections.Counter(my_dict).most_common(k)
        
        return [x[0] for x in most_common]