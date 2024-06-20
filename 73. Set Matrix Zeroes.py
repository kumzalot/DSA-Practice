class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerosRow = []
        zerosCol = []

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if (matrix[i][j] == 0):
                    zerosRow.append(i)
                    zerosCol.append(j)

        for r in range(len(zerosRow)):
            for c in range(n):
                matrix[zerosRow[r]][c] = 0
                
        for a in range(len(zerosCol)):
            for b in range(m):
                matrix[b][zerosCol[a]] = 0
        
