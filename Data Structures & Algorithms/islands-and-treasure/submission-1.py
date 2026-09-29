class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visited = set()
        queue = deque()

        def addVertex(r, c): 
            if r<0 or c<0 or r>=num_rows or c>=num_cols or grid[r][c]==-1 or(r,c) in visited: 
                return 
            visited.add((r,c))
            queue.append([r,c])


        for r in range(num_rows): 
            for c in range(num_cols):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                for dr, dc in directions: 
                    addVertex(r+dr, c+dc)
            dist += 1
             