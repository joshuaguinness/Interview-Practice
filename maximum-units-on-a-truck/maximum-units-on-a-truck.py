class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # Fill up the truck in order of largest
        # number of units per box. Greedy algorithm,
        # will always result in max number of units on
        # the truck
        
        # Sort by units / box
        boxTypes.sort(key = lambda x:x[1], reverse=True)
        
        output = 0
        
        for i, v in enumerate(boxTypes):
            
            # No more space on the truck
            if truckSize == 0:
                break
                
            # Number of boxes to add to the truck of
            # this box type
            num_boxes = min(truckSize, boxTypes[i][0])
            
            output += num_boxes * boxTypes[i][1]
            truckSize -= num_boxes
            
        return output