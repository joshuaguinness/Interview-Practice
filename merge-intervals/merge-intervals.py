class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort the intervals on the first element
        intervals.sort(key=lambda item: item[0])
        print(intervals)
        
        new_intervals = []
        
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            while i < len(intervals)-1 and end >= intervals[i+1][0]:
                end = max(intervals[i+1][1], end)
                i += 1
                
            new_intervals.append([start, end])
            i += 1
            
        return new_intervals
                
            
                