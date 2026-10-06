class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}

        for from_i, to_i, price_i in flights: 
            adj[from_i].append((to_i, price_i))

        visited = set() 
        heap = [(0, src, 0)]
        distances = [float("inf")] * n
        stops = [0] * n
        print(stops)

        while heap: 
            price, node, num_stops = heapq.heappop(heap)
            if node == dst: 
                return price
            if num_stops > k or num_stops>distances[node]: 
                continue
            distances[node] = num_stops
            for nei, price_j in adj[node]: 
                heapq.heappush(heap, (price+price_j, nei, num_stops+1))
        return -1


        