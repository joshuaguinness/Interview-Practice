class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if (firstList == [] or secondList == []):
            return []
        
        result = []
        i, j = 0, 0
        
        while (i < len(firstList) and j < len(secondList)):
            # Gets the start of possible intersection
            lower = max(firstList[i][0], secondList[j][0])
            # Gets the end of possible intersection
            higher = min(firstList[i][1], secondList[j][1])
            
            # If start <= end, then there is an intersection
            if lower <= higher:
                result.append([lower, higher])
               
            # Move to the next interval based on who has smallest endpoint
            if (firstList[i][1] < secondList[j][1]):
                i += 1
            else:
                j += 1
                
        return result
        
        
        # Initial method. Correct but "Memory Limit Exceeded"
        # arraySize = max(firstList + secondList, key=lambda x:x[1])[1]
        # coverageFirst = [0]*(arraySize+1)
        # coverageSecond = [0]*(arraySize+1)        
        # for i, v in enumerate(firstList):
        #     for j in range(v[0],v[1]):
        #         coverageFirst[j] = 1
        # for i, v in enumerate(secondList):
        #     for j in range(v[0],v[1]):
        #         coverageSecond[j] = 1
        # result = []
        # tracking = False
        # start, end = 0, 0
        # for i, v in enumerate(coverageFirst):
        #     if not tracking:
        #         if i > 0:
        #             if (v == 1 and coverageFirst[i-1] == 0 and coverageSecond[i] == 0 and coverageSecond[i-1] == 1):
        #                 result.append([i,i])
        #             elif (v == 0 and coverageFirst[i-1] == 1 and coverageSecond[i] == 1 and coverageSecond[i-1] == 0):
        #                 result.append([i,i])
        #         if (v == 1 and v == coverageSecond[i]):
        #             start = i
        #             tracking = True
        #     if tracking:
        #         if (v == 0 or coverageSecond[i] == 0):
        #             end = i
        #             result.append([start, end])
        #             tracking = False
        # return result       