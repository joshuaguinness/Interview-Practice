class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        length_heights = len(heights)
        max_height = heights[-1]
        buildings_set = {length_heights-1}        
        
        for i in range(2,len(heights)+1):
            if heights[-i] > max_height:
                buildings_set.add(length_heights-i)
                max_height = heights[-i]
                
        return sorted(buildings_set)