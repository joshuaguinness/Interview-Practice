class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # Fill up the truck in order of largest
        # number of units per box
        
        # Sort by units / box
        boxTypes.sort(key = lambda x:x[1], reverse=True)
        # print(boxTypes)
        
        output = 0
        
        i = 0
        # while truckSize > 0:
        #     # if truckSize - boxTypes[i][0] >= 0:
        #     #     output += boxTypes[i][0] * boxTypes[i][1]
        #     num_boxes = min(truckSize, boxTypes[i][0])
        #     output += num_boxes * boxTypes[i][1]
        #     truckSize -= num_boxes
        #     i += 1
        for i, v in enumerate(boxTypes):
            if truckSize == 0:
                break
            num_boxes = min(truckSize, boxTypes[i][0])
            output += num_boxes * boxTypes[i][1]
            truckSize -= num_boxes
        return output