class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_y = len(board)
        max_x = len(board[0])
        path = set()
        
        def dfs(y, x, i):
            if i == len(word): 
                return True
            if (x < 0) or (y < 0) or (x >= max_x) or (y >= max_y) or (y,x) in path or (board[y][x] != word[i]): 
                return False
            path.add((y,x))
            res = (dfs(y+1, x, i+1) or 
            dfs(y-1, x, i+1) or 
            dfs(y, x+1, i+1) or 
            dfs(y, x-1, i+1))
            path.remove((y,x))

            return res

        for i, row in enumerate(board): 
            for j, letter in enumerate(row): 
                if letter == word[0]:
                    if dfs(i, j, 0): 
                        return True

        return False


        