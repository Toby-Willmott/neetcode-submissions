class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific = set() 
        atlantic = set()

        pacific_start = []
        atlantic_start = []

        for row in range(num_rows): 
            for col in range(num_cols): 
                if row == 0 or col == 0: 
                    pacific_start.append((row, col))
                if row == num_rows - 1 or col == num_cols - 1:
                    atlantic_start.append((row, col))
        
        def dfs_pacific(row, col, prev): 
            if row<0 or col<0 or row>=num_rows or col>=num_cols or (row, col) in pacific or heights[row][col] < prev: 
                return
            pacific.add((row, col))
            for dr, dc in directions: 
                dfs_pacific(row + dr, col + dc, heights[row][col])

        def dfs_atlantic(row, col, prev): 
            if row<0 or col<0 or row>=num_rows or col>=num_cols or (row, col) in atlantic or heights[row][col] < prev: 
                return
            atlantic.add((row, col))
            for dr, dc in directions: 
                dfs_atlantic(row + dr, col + dc, heights[row][col])

        dfs_pacific(0,4,0)
        for row, col in pacific_start: 
            dfs_pacific(row, col, 0)
        
        for row, col in atlantic_start: 
            dfs_atlantic(row, col, 0)

        res = []
        for row in range(num_rows): 
            for col in range(num_cols): 
                if (row, col) in pacific and (row, col) in atlantic: 
                    res.append([row,col])
        return res




        


        