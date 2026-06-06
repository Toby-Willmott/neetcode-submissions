class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        for i in range(len(board)):
            d = {}
            for num in board[i]:
                if num in d: 
                    return False
                if num != ".": 
                    d[num] = 0
        for i in range(len(board)):
            d = {} 
            for j in range(len(board)):
                if board[j][i] in d: 
                    return False
                if board[j][i] != ".":
                    d[board[j][i]] = 0
        
     
        for col_l in range(0, 9, 3):
            for row_l in range(0, 9, 3):
                d = {}
                for col in range(3): 
                    for row in range(3): 
                        if board[row_l + row][col_l + col] in d:
                            return False
                        if board[row_l + row][col_l + col] != ".":
                            d[board[row_l + row][col_l + col]] = 0
            
        return True



        