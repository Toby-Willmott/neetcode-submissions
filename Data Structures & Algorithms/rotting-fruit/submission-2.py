class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        fresh = 0
        
        q = deque()
        

        def addCell(r, c): 
            nonlocal fresh
            if r<0 or c<0 or r>=num_rows or c>=num_cols or grid[r][c] != 1: 
                return
            grid[r][c] = 2
            q.append((r,c))
            fresh-=1
            

        for r in range(num_rows): 
            for c in range(num_cols): 
                if grid[r][c] == 2: 
                    q.append((r,c))
                if grid[r][c] == 1: 
                    fresh+=1
                
        time = 0
        while q and fresh: 
            time += 1
            for i in range(len(q)): 
                r, c = q.popleft() 
                for dr, dc in directions: 
                    addCell(r+dr, c+dc)
            
        if fresh: 
            return -1
        return time




                
        