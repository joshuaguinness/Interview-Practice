class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Iterate through the array
        # Add to a new array the distance
        # then return max(distance array) k times
        
        distances = []
        
        for i, v in enumerate(points):
            distances.append((i, v[0]**2 + v[1]**2))
            
        distances.sort(key=lambda x:x[1])
        min_distances = []
        for i in range(k):
            min_distances.append(points[distances[0][0]])
            distances.pop(0)
            
        return min_distances
            
        
        
        