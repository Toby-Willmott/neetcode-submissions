import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(x*x + y*y), x, y) for x, y in points]
        heapq.heapify(distances)

        output = [] 
        while len(output) < k: 
            dis, x, y = heapq.heappop(distances)
            output.append([x, y])
        
        return output