class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zeros_row, zeros_col = [], []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros_row.append(i)
                    zeros_col.append(j)
        
        # to change the columns in a ROW
        for row in range(len(zeros_row)):
            for col in range(n):
                matrix[zeros_row[row]][col] = 0
        
        # to change the rows in a COLUMN
        for col in range(len(zeros_col)):
            for row in range(m):
                matrix[row][zeros_col[col]] = 0
        