class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Iterate through the array
        # Add to a new array the distance
        # Sort the array based on distance
        # Return the first element of the array k times, popping the first element each time
        
#         distances = []
        
#         for i, v in enumerate(points):
#             distances.append((i, v[0]**2 + v[1]**2))
            
#         distances.sort(key=lambda x:x[1])
#         min_distances = []
#         for i in range(k):
#             min_distances.append(points[distances[0][0]])
#             distances.pop(0)
            
#         return min_distances


        # Using a PQ and list comprehension
        # Create a PQ for all the points
        distances = [(v[0]**2 + v[1]**2, i) for i, v in enumerate(points)]
        heapq.heapify(distances)

        # Return the points as a list from the k shortest distances
        return [points[i[1]] for i in heapq.nsmallest(k, distances)]
