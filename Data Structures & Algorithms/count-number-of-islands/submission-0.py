class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])
        islands = 0

        def dfs(r, c): 
            if r<0 or c<0 or r>=NUM_ROWS or c>=NUM_COLS or grid[r][c] == "0": 
                return
            
            grid[r][c] = "0"
            for dr, dc in directions: 
                dfs(r + dr ,c +  dc)
            
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS): 
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands