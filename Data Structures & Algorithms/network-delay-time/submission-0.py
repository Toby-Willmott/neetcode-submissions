class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        d = [float("inf")] * len(times)
        pi = [None] * len(times)

        for u, v, w in times: 
            edges[u].append((v,w))

        minHeap = [(0, k)]
        visited = set() 
        t = 0

        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node in visited: 
                continue 
            visited.add(node)
            t = dist

            for node2, dist2 in edges[node]: 
                if node2 not in visited: 
                    heapq.heappush(minHeap, (dist+dist2, node2))
        return t if len(visited) == n else -1



        
        