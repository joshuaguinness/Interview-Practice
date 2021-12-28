class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort the intervals on the first element
        intervals.sort(key=lambda item: item[0])
        
        n = len(intervals)
        new_intervals = []
        
        i = 0
        # Iterate through the intervals array
        while i < n:
            
            # Current interval to add to the array is start and end
            # of current interval
            start = intervals[i][0]
            end = intervals[i][1] 
            
            # If the end of the current element is larger than the
            # start of the next element, and its not at the end of
            # the array, there is an overlap
            
            # Modify the end to be the max of the current
            # end and the end of the next interval
            while i < n-1 and end >= intervals[i+1][0]:
                end = max(intervals[i+1][1], end)
                i += 1
                
            # Add new interval to array
            new_intervals.append([start, end])
            i += 1
            
        return new_intervals