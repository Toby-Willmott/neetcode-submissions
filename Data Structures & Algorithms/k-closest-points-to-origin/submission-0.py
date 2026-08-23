import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [(math.sqrt(x**2 + y**2), x, y) for x, y in points]
        heapq.heapify(distance)

        output = []
        while len(output) < k: 
            dis, x, y = heapq.heappop(distance)
            output.append([x, y])

        return output
        