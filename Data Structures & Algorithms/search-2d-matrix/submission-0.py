class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        top_row = 0 
        bottom_row = num_rows-1 

        while top_row <= bottom_row: 
            index = (top_row + bottom_row)//2
            row = matrix[index]
            if row[0] < target and row[-1] < target: 
                top_row = index + 1
            elif row[0] > target and row [-1] > target: 
                bottom_row = index - 1
            else: 
                break

        if not(top_row <= bottom_row): 
            return False
        
        l = 0
        r = num_cols -1

        while l <= r: 
            m = (l+r) // 2
            test = matrix[index][m]

            if test < target: 
                l = m +1
            elif test > target: 
                r = m-1 
            else: 
                return True
        return False

            

        