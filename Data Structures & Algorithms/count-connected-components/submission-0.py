class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num = 0 
        connected = {i: [] for i in range(n)}
        for a, b in edges: 
            connected[a].append(b)
            connected[b].append(a)

        visited = set() 

        def dfs(node, prev): 
            if node in visited: 
                return
            
            visited.add(node)
            for nei in connected[node]:
                if nei == prev: 
                    continue 
                dfs(nei, node)
            
        for n in range(n): 
            if n not in visited: 
                num+=1
                dfs(n, -1)

        return num



        