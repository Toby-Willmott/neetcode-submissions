class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(row, col): 
            if row<0 or col<0 or row>=num_rows or col>=num_cols or board[row][col] != "O":
                return 
            board[row][col] = "T"
            for dr, dc in directions: 
                dfs(row+dr, col+dc)
            return 
        
        for row in range(num_rows): 
            dfs(row, 0)
            dfs(row, num_cols-1)
        for col in range(num_cols):
            dfs(0, col)
            dfs(num_rows-1, col)
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c]=="T":
                    board[r][c] = "O"
                elif board[r][c]=="O":
                    board[r][c]="X"

        