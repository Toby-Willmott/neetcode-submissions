class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        connection = {i: [] for i in range(n+1)}

        for a, b in edges: 
            connection[a].append(b)
            connection[b].append(a)

        visited = set() 
        cycle = set()
        cycleStart = -1 

        def dfs(node, prev): 
            nonlocal cycleStart
            if node in visited: 
                cycleStart = node
                return True
            
            visited.add(node)

            for nei in connection[node]: 
                if nei == prev: 
                    continue
                if dfs(nei, node):
                    if cycleStart != -1: 
                        cycle.add(nei)
                    if node == cycleStart: 
                        cycleStart = -1 
                    return True 
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
             if u in cycle and v in cycle: 
                return [u,v]
        return []

            
        