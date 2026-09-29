class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_rows = len(grid)
        max_cols = len(grid[0])
        max_island = 0 
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        

        def dfs(r, c, cur_length):
            if r < 0 or c < 0 or r >= max_rows or c >= max_cols or grid[r][c] == 0: 
                return cur_length
            
            grid[r][c] = 0
            cur_length += 1
            for dr, dc in directions: 
                cur_length = dfs(r + dr, c + dc, cur_length)
            return cur_length
        
        for row in range(max_rows): 
            for col in range(max_cols): 
                if grid[row][col] == 1:
                    cur_length = dfs(row, col, 0)
                    max_island = max(max_island, cur_length)
                    
        return max_island
