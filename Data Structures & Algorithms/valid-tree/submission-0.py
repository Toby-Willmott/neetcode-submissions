class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1): 
            return False

        connected = {i: [] for i in range(n)}

        for a, b in edges: 
            connected[a].append(b)
            connected[b].append(a)
        
        visited = set() 

        def dfs(cur, par): 
            if cur in visited: 
                return False

            visited.add(cur)

            for node in connected[cur]:
                if node == par: 
                    continue 
                if not dfs(node, cur): 
                    return False
            return True

        return dfs(0, -1) and len(visited) == n 
            

        
        