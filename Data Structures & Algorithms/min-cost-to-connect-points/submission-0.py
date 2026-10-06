class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        
        for i in range(n): 
            xi, yi = points[i]
            for j in range(i+1, n):
                 xj, yj = points[j]
                 dist = abs(xi - xj) + abs(yi - yj)
                 adj[i].append([dist, j])
                 adj[j].append([dist, i])

        res = 0 
        connections = 0
        visited = set() 
        heap = [(0, 0)]

        while len(visited)<n: 
            #print("heap", heap)
            #print("visited", visited)
            dist, node = heapq.heappop(heap)
            if node in visited: 
                continue 
            visited.add(node)
            res += dist
            for wei, nei in adj[node]: 
                if nei not in visited: 
                    heapq.heappush(heap, (wei, nei))
        return res
            